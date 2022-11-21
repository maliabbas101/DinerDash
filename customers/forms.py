from django import forms
from .models.customer import Customer
from django.utils.translation import gettext_lazy as _



class CustomerForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())


    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Customer
        fields = ["email", "username", "full_name",
                  "password", "confirm_password", "phone_number", "groups"]



class CustomerLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Customer
        fields = ["email", "password"]
