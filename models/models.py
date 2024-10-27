from django.db import models
from django.dispatch import receiver
from django.utils.formats import date_format
import datetime
import os
import uuid

def calculate_string(text) -> int:
    print(int.from_bytes(bytes(text, 'utf-8'), byteorder='big'))
    return int.from_bytes(bytes(text, 'utf-8'), byteorder='big')



class PUBLICACION(models.Model):
    titulo = models.CharField(max_length=50, default="PLACEHOLDER TITLE")
    autor = models.ForeignKey("USUARIO",on_delete=models.CASCADE, default="USUARIO")
    descripcion = models.TextField(default="LOREMP PSIUM")
    categoria = models.ManyToManyField("CATEGORIA")
    fecha = models.DateField(default=datetime.date.today)
    archivos = models.ManyToManyField("MEDIA",related_name="files")
    portada = models.ForeignKey("MEDIA",on_delete=models.SET_NULL, null=True)
    dv = models.TextField(default="1")

    def renove_dv(self):
        buffer = calculate_string(getattr(self, "titulo"))
        print(int(getattr(self, "autor").dv))
        buffer += int(getattr(self, "autor").dv)
        print(getattr(self, "descripcion"))
        buffer += calculate_string(getattr(self, "descripcion"))
        print(date_format(getattr(self, "fecha")))
        buffer += calculate_string(date_format(getattr(self, "fecha")))
        print(getattr(self, "categoria").all())
        for i in getattr(self, "categoria").all():
            buffer += i.dv
        print(getattr(self, "archivos").all())
        for i in getattr(self, "archivos").all():
            buffer += i.dv
        print(getattr(self, "portada"))
        buffer += getattr(self, "portada").dv
        print(str(buffer))
        self.dv = str(buffer)
        print(self.dv)
        self.save()
        return buffer

class USUARIO(models.Model):
    nombre = models.CharField(max_length=50,default="PLACEHOLDER NAME")
    gmail = models.EmailField(default="PLACEHOLDER GMAIL")
    contrasena = models.CharField(max_length=30, default="PLACEHOLDER PASSWORD")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dv = models.TextField(default="1")

    def renove_dv(self):
        buffer = calculate_string(getattr(self, "nombre"))
        print(getattr(self, "gmail"))
        buffer += calculate_string(getattr(self, "gmail"))
        print(getattr(self, "contrasena"))
        buffer += calculate_string(getattr(self, "contrasena"))
        print(str(buffer))
        self.dv = str(buffer)
        print(self.dv)
        self.save()
        return buffer

class MEDIA(models.Model):
    archivo = models.FileField(upload_to="media/")
    dv = models.TextField(default="1")

    def renove_dv(self):
        buffer = calculate_string(getattr(self, "archivo").name)
        print(str(buffer))
        self.dv = str(buffer)
        print(self.dv)
        self.save()
        return buffer


@receiver(models.signals.post_delete, sender=MEDIA)
def on_delete(sender, instance, **kargs):

    if instance.archivo:

        if os.path.isfile(instance.archivo.path):

            os.remove(instance.archivo.path)

class CATEGORIA(models.Model):
    nombre = models.CharField(max_length=50)
    dv = models.TextField(default="1")

    def renove_dv(self):
        buffer = calculate_string(getattr(self, "nombre"))
        print(str(buffer))
        self.dv = str(buffer)
        print(self.dv)
        self.save()
        return buffer

class DIGITOS_VERIFICADORES(models.Model):
    tabla = models.CharField(max_length=50)
    dv = models.TextField(default="1")

    def actualize_table(self):
        data = 0
        if self.tabla == "USUARIO":
            for i in USUARIO.objects.all():
                data += i.renove_dv()
        elif self.tabla == "MEDIA":
            for i in MEDIA.objects.all():
                data += i.renove_dv()
        elif self.tabla == "CATEGORIA":
            for i in CATEGORIA.objects.all():
                data += i.renove_dv()
        elif self.tabla == "PUBLICACION":
            for i in PUBLICACION.objects.all():
                data += i.renove_dv()
        self.dv = data
        self.save()
