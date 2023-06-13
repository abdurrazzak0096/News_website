from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from website.models import Comment, Contact


class RegisterForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class LoginForms(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=32)


class CommentForm(forms.Form):
    class Meta:
        model = Comment
        fields = ('comment',)


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

