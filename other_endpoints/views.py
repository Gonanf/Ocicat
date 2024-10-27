from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from models.models import CATEGORIA, USUARIO,DIGITOS_VERIFICADORES

def get_categories():
    if not DIGITOS_VERIFICADORES.verify_dv_page():
        return render(request,'DV_page/dv.html')
    return CATEGORIA.objects.all()

def get_autors():
    if not DIGITOS_VERIFICADORES.verify_dv_page():
        return render(request,'DV_page/dv.html')
    return USUARIO.objects.all()

def categoria(request):
    if not DIGITOS_VERIFICADORES.verify_dv_page():
        return render(request,'DV_page/dv.html')
    return JsonResponse({'categorias': [categoria.nombre for categoria in CATEGORIA.objects.all()]}, safe=False)
