from django.contrib import admin

from user.models import (
    User,
    UserAddress,
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
        'phone',
        'datetime_of_birth',
        'score_balance',
        'priority',
        'is_deleted',
        'gender',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_deleted',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'first_name',
        'last_name',
        'email',
        'phone',
    )


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'title',
        'phone_number',
        'country',
        'pincode',
        'is_default',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_default',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'user__first_name',
        'user__last_name',
        'user__email',
        'user__phone',
    )
