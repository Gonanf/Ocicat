from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from models.models import CATEGORIA

def categoria(request):
    return JsonResponse({'categorias': [categoria.nombre for categoria in CATEGORIA.objects.all()]}, safe=False)