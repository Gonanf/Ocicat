from django.contrib import admin
from .models import PUBLICACION,USUARIO,MEDIA,CATEGORIA
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
