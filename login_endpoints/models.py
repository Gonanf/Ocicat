from django.db import models
from django import forms
<<<<<<< HEAD
import uuid
=======
>>>>>>> 5c9b7b9121a59bb699ce20b0520db7fbe56cd372

class Login(forms.Form):
    gmail = forms.EmailField()
    contrasena = forms.CharField(max_length=30)
<<<<<<< HEAD
    pk = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
=======

>>>>>>> 5c9b7b9121a59bb699ce20b0520db7fbe56cd372
