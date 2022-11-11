from django import forms
from .models.customer import Customer


class CustomerForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Customer
        fields = "__all__"
