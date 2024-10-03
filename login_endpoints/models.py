from django.db import models
from django import forms

class Login(forms.Form):
    gmail = forms.EmailField()
    contrasena = forms.CharField(max_length=30)

