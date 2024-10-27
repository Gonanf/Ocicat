from django.contrib import admin
from .models import PUBLICACION,USUARIO,MEDIA,CATEGORIA,DIGITOS_VERIFICADORES
# Register your models here.



@admin.action(description="Actualize DV")
def actualize_DV(modeladmin, request, queryset):
    modelos = queryset.all()
    for m in modelos:
        m.renove_dv()

@admin.action(description="Actualize DV table")
def actualize_DV_table(modeladmin, request, queryset):
    modelos = queryset.all()
    for m in modelos:
        m.actualize_table()

class USUARIO_ADMIN(admin.ModelAdmin):
    list_display = ['nombre']
    actions = [actualize_DV]

admin.site.register(USUARIO, USUARIO_ADMIN)

@admin.register(MEDIA)
class MEDIA_ADMIN(admin.ModelAdmin):
    list_display = ['archivo']
    actions = [actualize_DV]


@admin.register(CATEGORIA)
class CATEGORIA_ADMIN(admin.ModelAdmin):
    list_display = ['nombre']
    actions = [actualize_DV]

@admin.register(PUBLICACION)
class PUBLICACION_ADMIN(admin.ModelAdmin):
    list_display = ['titulo']
    actions = [actualize_DV]

@admin.register(DIGITOS_VERIFICADORES)
class DIGITOS_VERIFICADORES_ADMIN(admin.ModelAdmin):
    list_display = ['tabla']
    actions = [actualize_DV_table]
