from django.contrib import admin

from products.models import (
    Product,
    ProductCategory,
    ProductCategoryFaq,
    ProductFaq,
    ProductImage,
    ProductProvider,
    ProductCategoryImage,
)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'sub_title',
        'priority',
        'is_active',
        'is_upcoming',
        'is_deliverable',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
        'is_upcoming',
        'is_deliverable',
        'created_at',
        'updated_at',
    )
    search_fields = ('title', 'sub_title',)
    readonly_fields = ('slug', )


@admin.register(ProductCategoryImage)
class ProductCategoryImageAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'image',
        'is_approved',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'category',
        'is_approved',
        'created_at',
        'updated_at',
    )
    search_fields = ('category__title',)
    

@admin.register(ProductCategoryFaq)
class ProductCategoryFaqAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'question',
        'answer',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'category',
        'created_at',
        'updated_at',
    )
    search_fields = ('category__title',)
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'priority',
        'price',
        'offer_price',
        'is_active',
        'list_product',
        'custom_product',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'category',
        'is_active',
        'list_product',
        'custom_product',
        'created_at',
        'updated_at',
    )
    search_fields = ('category__title', 'title')
    

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'image',
        'is_approved',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_approved',
        'created_at',
        'updated_at',
    )
    search_fields = ('product__title', )


@admin.register(ProductFaq)
class ProductFaqAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'question',
        'answer',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'product',
        'created_at',
        'updated_at',
    )
    search_fields = ('product__title',)


@admin.register(ProductProvider)
class ProductProviderAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'price',
        'offer_price',
        'new_offer_price',
        'is_approved',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_approved',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'product__title',
        'user__first_name',
        'user__last_name',
        'user__email',
        'user__phone',
    )