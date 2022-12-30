from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.modelfields import PhoneNumberField
from user.models import User


class NewUserForm(UserCreationForm):
    phone = PhoneNumberField()

    class Meta:
        model = User
        fields = ("phone", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
