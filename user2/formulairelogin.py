from django import forms
from django.contrib.auth.forms import AuthenticationForm


class login(AuthenticationForm):
        username = forms.CharField(label='nom utilisateur', max_length=100)
        password = forms.CharField(label='mot de passe', widget=forms.PasswordInput)