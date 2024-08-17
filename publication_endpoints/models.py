from django.db import models
from django import forms

class Publication_Data(forms.Form):
    titulo = forms.CharField(max_length=50)
    descripcion = forms.TextInput()
    portada = forms.FileField()
    categorias = forms.JSONField()
    archivos = forms.JSONField()

