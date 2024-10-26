from django.contrib import admin
from .models import PUBLICACION,USUARIO,MEDIA,CATEGORIA,DIGITOS_VERIFICADORES
# Register your models here.
class USUARIO_ADMIN(admin.ModelAdmin):
    list_display = ['nombre']

admin.site.register(USUARIO, USUARIO_ADMIN)


@admin.register(MEDIA)
class MEDIA_ADMIN(admin.ModelAdmin):
    list_display = ['archivo']


@admin.register(CATEGORIA)
class CATEGORIA_ADMIN(admin.ModelAdmin):
    list_display = ['nombre']

@admin.register(PUBLICACION)
class PUBLICACION_ADMIN(admin.ModelAdmin):
    list_display = ['titulo']

@admin.register(DIGITOS_VERIFICADORES)
class DIGITOS_VERIFICADORES_ADMIN(admin.ModelAdmin):
    list_display = ['tabla']
