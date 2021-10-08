from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "name")