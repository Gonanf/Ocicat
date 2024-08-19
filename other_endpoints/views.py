from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from models.models import CATEGORIA, USUARIO

def get_categories():
    return CATEGORIA.objects.all()

def get_autors():
    return USUARIO.objects.all()

def categoria(request):
    return JsonResponse({'categorias': [categoria.nombre for categoria in CATEGORIA.objects.all()]}, safe=False)