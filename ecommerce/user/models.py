from django.db import models
from sorl.thumbnail import ImageField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _
# from django.utils.html import mark_safe
from django.contrib.auth.hashers import make_password
import string    
import random

from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings


class Avatar(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    image = ImageField(upload_to='upload/images/users/avatar/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # def image_preview(self):
    #     return mark_safe('<img src="%s" width="100" height="100" />' % (self.image))


class AbstractUser(models.Model):
    def generate_password():
        password = "dfghjk"
        return password
    
    avatar = models.ForeignKey(Avatar,
                               related_name="users",
                               on_delete=models.CASCADE,
                               null=True)
    password = models.CharField(max_length=100, default=generate_password())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        self.password = make_password((self.password))
        super(AbstractUser, self).save(*args, **kwargs)


class User(AbstractUser):
    class Gender_Choice(models.IntegerChoices):
        UNKNOWN = 0, _("Unknown")
        MALE = 1, _("Male")
        FEMALE = 2, _("Female")

    class Priority_Choices(models.IntegerChoices):
        HIGH_PRIORITY = 0, _("High Priority")
        NORMAL_PRIORITY = 1, _("Normal Priority")
        LOW_PRIORITY = 2, _("Low Priority")

    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    phone = PhoneNumberField()
    datetime_of_birth = models.DateTimeField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    gender = models.PositiveIntegerField(
        choices=Gender_Choice.choices,
        default=Gender_Choice.UNKNOWN)
    priority = models.PositiveIntegerField(
        choices=Priority_Choices.choices,
        default=Priority_Choices.NORMAL_PRIORITY)
    score_balance = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    @property
    def user_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name}_{self.last_name}_{self.pk}"
        return f"unknown_{self.pk}"

    def get_full_name(self):
        if self.first_name or self.last_name:
            return self.first_name + " " + self.last_name
        return None

    def __str__(self):
        return self.email


class UserAddress(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="address")
    title = models.CharField(max_length=200, null=True, blank=True)
    phone_number = PhoneNumberField()
    alt_phone_number = PhoneNumberField(null=True, blank=True)
    address = models.TextField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    pincode = models.CharField(max_length=8)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.title}"
