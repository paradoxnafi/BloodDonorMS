from django.forms import ModelForm
from django import forms
from .models import Register


class RegisterForm(ModelForm):
    class Meta:
        model = Register
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
           }
        fields = ['username', 'name', 'email', 'password1', 'password2', 'contact_number']