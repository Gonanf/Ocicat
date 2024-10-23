from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from models.models import CATEGORIA, USUARIO

def get_categories():
    return CATEGORIA.objects.all()

def get_autors():
    return USUARIO.objects.all()

def categoria(request):
    return JsonResponse({'categorias': [categoria.nombre for categoria in CATEGORIA.objects.all()]}, safe=False)

class ManagerDigitos:
    def init_dv():
        pass

    def actualize_dv(table):
        pass
    
    def check_dv(table):
        pass

    def check_whole():
        pass
