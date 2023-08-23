from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    username = forms.CharField(required=True, min_length=4)
    first_name = forms.CharField(required=True, min_length=4)
    last_name = forms.CharField(required=True, min_length=4)
    email = forms.EmailField(required=True, min_length=4)
    password = forms.CharField(required=True, min_length=4)
    password1 = forms.CharField(required=False, min_length=4)
    password2 = forms.CharField(required=False, min_length=4,)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, required=True)
    password = forms.CharField(max_length=65,min_length=4, widget=forms.PasswordInput)