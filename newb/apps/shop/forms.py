from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomerRegisterForm(UserCreationForm):
    address = forms.CharField()
    postal_code = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    phone = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
