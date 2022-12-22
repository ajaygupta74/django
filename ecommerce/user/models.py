from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _


class User(models.Model):
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
    score_balance = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    gender = models.PositiveIntegerField(
        choices=Gender_Choice.choices,
        default=Gender_Choice.UNKNOWN)
    priority = models.PositiveIntegerField(
        choices=Priority_Choices.choices,
        default=Priority_Choices.NORMAL_PRIORITY)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    