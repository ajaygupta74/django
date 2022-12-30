from django.db import models
from sorl.thumbnail import ImageField
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError


from user.models import User


class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_deliverable = models.BooleanField(default=False)
    priority = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_upcoming = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.priority is None:
            last_category = ProductCategory.objects.last()
            self.priority = last_category.id + 1
        if self.slug is None:
            self.slug = slugify(self.title)
        super(ProductCategory, self).save(*args, **kwargs)


class ProductCategoryImage(models.Model):
    category = models.ForeignKey(ProductCategory,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 related_name='images')
    image = ImageField(
        upload_to='upload/images/products/product-category-images/')
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductCategoryFaq(models.Model):
    category = models.ForeignKey(ProductCategory,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 related_name='faqs')
    question = models.CharField(max_length=250)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    description = RichTextField(
        config_name='awesome_ckeditor', null=True, blank=True)
    category = models.ForeignKey(ProductCategory,
                                 on_delete=models.CASCADE,
                                 related_name='products')
    is_deliverable = models.BooleanField(default=False)
    priority = models.PositiveIntegerField(null=True, blank=True)
    consultants = models.ManyToManyField(
        User,
        through='ProductProvider',
        related_name='products')
    price = models.DecimalField(decimal_places=2,
                                max_digits=10,
                                default=0)
    offer_price = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=10, default=0)
    is_active = models.BooleanField(default=True)
    list_product = models.BooleanField(
        default=True,
        help_text="Whether to show product in listing or not")
    custom_product = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def discount(self):
        return ((100 - round((self.offer_price / self.price) * 100))
                if self.offer_price and self.price else 0)

    def clean(self):
        if self.offer_price is not None and self.price is not None:
            if self.offer_price > self.price:
                raise ValidationError({
                    'offer_price': _('Should be less than price')})
        else:
            raise ValidationError({
                'offer_price': _('Price and Offer price is required')})

    def save(self, *args, **kwargs):
        last_product = Product.objects.last()
        if self.priority is None and self.custom_product is False:
            self.priority = last_product.id + 1
        if self.slug is None:
            product = Product.objects.filter(title=self.title)
            if product:
                self.slug = slugify(self.title + str(last_product.id + 1))
            else:
                self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def category_type_value(self):
        return (ProductCategory.CategoryType(
            self.category.category_type).name)
    category_type_value.short_description = 'category type'


class ProductImage(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                null=True,
                                related_name='images')
    image = ImageField(upload_to='upload/images/products/product-images/')
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductFaq(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                null=True,
                                related_name='faqs')
    question = models.CharField(max_length=250)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductProvider(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='users')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='assignedproducts')
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    offer_price = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=10, default=0)
    new_offer_price = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=10, default=0)
    is_approved = models.BooleanField(default=False)
    status_timeline = models.JSONField(default=list, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}: {self.product}"

    def clean(self):
        if self.offer_price is not None and self.price is not None:
            if self.offer_price > self.price:
                raise ValidationError({
                    'offer_price': _('Should be less than price')})
        else:
            raise ValidationError({
                'offer_price': _('Price and Offer price is required')})
