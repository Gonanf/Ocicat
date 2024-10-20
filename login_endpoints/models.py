from django.db import models
from django import forms

import uuid

class Login(forms.Form):
    gmail = forms.EmailField()
    contrasena = forms.CharField(max_length=30)

    pk = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

