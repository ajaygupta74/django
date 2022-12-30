from django.contrib import admin
from django.utils.html import format_html
# from sorl.thumbnail import get_thumbnail
import random
import string


from user.models import (
    User,
    Avatar,
    UserAddress,
)


@admin.register(Avatar)
class Avatar(admin.ModelAdmin):
    list_display = (
        'title',
        'is_active',
        'image',
        'created_at',
        'updated_at'
    )
    list_filter = (
        'is_active',
        'created_at',
        'updated_at',
    )
    # readonly_fields = ('imageview', )

    # def image_preview(self, obj):
    # if obj.image:
    #     imagepreview = get_thumbnail(obj.image,
    #                                  '150x150',
    #                                  upscale=False,
    #                                  crop=False)
    #     return format_html(
    #         '''<a href="{}" target="{}"><img src="{}"
    #          width="{}" height="{}"></a>'''
    #         .format(obj.image.url,
    #                 "_blank",
    #                 imagepreview.url,
    #                 imagepreview.width,
    #                 imagepreview.height))
    # return ""


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
    exclude = ('password', )

    # def save_model(self, request, obj, form):
    #     if self.password is None:
    #         self.password = ''.join(random.choices(string
    # .ascii_uppercase + string.digits, k = 6))
    #     return super().save_model(request, obj, form)

    # # def save(self):
    # #
    # #     return super().clean()


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
