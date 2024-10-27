from django.db import models
from django.dispatch import receiver
from django.utils.formats import date_format
import datetime
import os
import uuid

def calculate_string(text) -> int:
    buffer = 0
    for i in text:
        buffer += ord(i)
    return buffer

class PUBLICACION(models.Model):
    titulo = models.CharField(max_length=50, default="PLACEHOLDER TITLE")
    autor = models.ForeignKey("USUARIO",on_delete=models.CASCADE, default="USUARIO")
    descripcion = models.TextField(default="LOREMP PSIUM")
    categoria = models.ManyToManyField("CATEGORIA")
    fecha = models.DateField(default=datetime.date.today)
    archivos = models.ManyToManyField("MEDIA",related_name="files")
    portada = models.ForeignKey("MEDIA",on_delete=models.SET_NULL, null=True)
    dv = models.IntegerField(default=1)

    def renove_dv(self,saving):
        buffer = calculate_string(getattr(self, "titulo"))
        buffer += int(getattr(self, "autor").dv)
        buffer += calculate_string(getattr(self, "descripcion"))
        buffer += calculate_string(date_format(getattr(self, "fecha")))
        for i in getattr(self, "categoria").all():
            buffer += i.dv
        for i in getattr(self, "archivos").all():
            buffer += i.dv
        buffer += getattr(self, "portada").dv
        if saving:
            self.dv = buffer
            self.save()
            print(int(self.dv))
        return buffer

class USUARIO(models.Model):
    nombre = models.CharField(max_length=50,default="PLACEHOLDER NAME")
    gmail = models.EmailField(default="PLACEHOLDER GMAIL")
    contrasena = models.CharField(max_length=30, default="PLACEHOLDER PASSWORD")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dv = models.IntegerField(default=1)


    def renove_dv(self, saving):
        buffer = calculate_string(getattr(self, "nombre"))
        buffer += calculate_string(getattr(self, "gmail"))
        buffer += calculate_string(getattr(self, "contrasena"))
        if saving:
            self.dv = buffer
            self.save()

        return buffer

    def get_dv(self):
        print(int(self.dv))

class MEDIA(models.Model):
    archivo = models.FileField(upload_to="media/")
    dv = models.IntegerField(default=1)

    def renove_dv(self, saving):
        buffer = calculate_string(getattr(self, "archivo").name)
        if saving:
            self.dv = buffer
            self.save()
        return buffer
    def get_dv(self):
        print(int(self.dv))


@receiver(models.signals.post_delete, sender=MEDIA)
def on_delete(sender, instance, **kargs):

    if instance.archivo:

        if os.path.isfile(instance.archivo.path):

            os.remove(instance.archivo.path)

class CATEGORIA(models.Model):
    nombre = models.CharField(max_length=50)
    dv = models.IntegerField(default=1)

    def renove_dv(self, saving):
        buffer = calculate_string(getattr(self, "nombre"))
        if saving:
            self.dv = buffer
            self.save()
        return buffer

class DIGITOS_VERIFICADORES(models.Model):

    tabla = models.CharField(max_length=50)
    dv = models.IntegerField(default=1)

    def get_dv(self):
        print(int(self.dv))

    def actualize_table(self):
        data = 0
        if self.tabla == "USUARIO":
            for i in USUARIO.objects.all():
                data += i.dv
        elif self.tabla == "MEDIA":
            for i in MEDIA.objects.all():
                data += i.dv
        elif self.tabla == "CATEGORIA":
            for i in CATEGORIA.objects.all():
                data += i.dv
        elif self.tabla == "PUBLICACION":
            for i in PUBLICACION.objects.all():
                data += i.dv
        self.dv = data
        print(int(data))
        self.save()
        print(int(self.dv))

    def verify_dv(self):
        dv = 0
        if self.tabla == "USUARIO":
            for i in USUARIO.objects.all():
                dv += i.renove_dv(False)
        elif self.tabla == "MEDIA":
            for i in MEDIA.objects.all():
                dv +=  i.renove_dv(False)
        elif self.tabla == "CATEGORIA":
            for i in CATEGORIA.objects.all():
                dv +=  i.renove_dv(False)
        elif self.tabla == "PUBLICACION":
            for i in PUBLICACION.objects.all():
                dv +=  i.renove_dv(False)
        print(self.tabla)
        print(dv)
        print(int(self.dv))
        return dv == int(self.dv)

    def verify_dv_page():
        print(PUBLICACION.objects.all())
        for i in DIGITOS_VERIFICADORES.objects.all():
            if not i.verify_dv():
                return False
        return True
