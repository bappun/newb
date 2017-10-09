from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from newb.apps.shop.models import Contact, Customer


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class CustomerRegisterForm(forms.ModelForm):

    class Meta:
        model = Customer
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(CustomerRegisterForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
