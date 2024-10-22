from django.db import models
from django.dispatch import receiver
import datetime
import os

class PUBLICACION(models.Model):
    titulo = models.CharField(max_length=50, default="PLACEHOLDER TITLE")
    autor = models.ForeignKey("USUARIO",on_delete=models.CASCADE, default="USUARIO")
    descripcion = models.TextField(default="LOREMP PSIUM")
    categoria = models.ManyToManyField("CATEGORIA")
    fecha = models.DateField(default=datetime.date.today)
    archivos = models.ManyToManyField("MEDIA",related_name="files")
    portada = models.ForeignKey("MEDIA",on_delete=models.SET_NULL, null=True)

class USUARIO(models.Model):
    nombre = models.CharField(max_length=50,default="PLACEHOLDER NAME")
    gmail = models.EmailField(default="PLACEHOLDER GMAIL")
    contrasena = models.CharField(max_length=30, default="PLACEHOLDER PASSWORD")

class MEDIA(models.Model):
    archivo = models.FileField(upload_to="media/")

    
@receiver(models.signals.post_delete, sender=MEDIA)
def on_delete(sender, instance, **kargs):
    print("elimiando")
    if instance.archivo:
        print("existe")
        if os.path.isfile(instance.archivo.path):
            print("eliminao")
            os.remove(instance.archivo.path)

class CATEGORIA(models.Model):
    nombre = models.CharField(max_length=50)



