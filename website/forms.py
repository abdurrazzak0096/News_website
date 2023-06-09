from django import forms
from django.contrib.auth.models import User


class RegisterForms(forms.ModelForm):
    class Meta:

        model = User
        fields = ('username', 'email', 'password')


class LoginForms(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=32)