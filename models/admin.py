from django.contrib import admin
from .models import PUBLICACION,USUARIO,MEDIA,CATEGORIA,DIGITOS_VERIFICADORES
# Register your models here.



@admin.action(description="Actualize DV")
def actualize_DV(modeladmin, request, queryset):
    modelos = queryset.all()
    for m in modelos:
        m.renove_dv(True)

@admin.action(description="get DV")
def get_dvtable_dv(modeladmin, request, queryset):
    modelos = queryset.all()
    for m in modelos:
        m.get_dv()

@admin.action(description="Actualize DV table")
def actualize_DV_table(modeladmin, request, queryset):
    modelos = queryset.all()
    for m in modelos:
        m.actualize_table()

@admin.action(description="Actualize all the DV tables")
def actualize_all_DV_table(modeladmin, request, queryset):
    for i in DIGITOS_VERIFICADORES.objects.all():
        i.actualize_table()

@admin.action(description="Verify DV table")
def verify_DV_table(modeladmin, request, queryset):
    modelos = queryset.all()
    for m in modelos:
        m.verify_dv()

class USUARIO_ADMIN(admin.ModelAdmin):
    list_display = ['nombre']
    actions = [actualize_DV,get_dvtable_dv]

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
    actions = [actualize_DV_table,actualize_all_DV_table,get_dvtable_dv]
