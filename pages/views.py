import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models.models import CATEGORIA, PUBLICACION
from login_endpoints.views import find_user, USUARIO
from publication_endpoints.views import get_publication_by_id

def index(request):
    return render(request,'main_page/index.html')

def login(request):
    return render(request,'login_page/login.html')

def publication(request, type):
    if (type == "new"):
        usuario = find_user(request)
        if (usuario is HttpResponseNotFound):
            return usuario
        return render(request,'P_publication_page/post_publication.html', context={'categorias': [categoria.nombre for categoria in CATEGORIA.objects.all()], 'usuario': usuario.nombre})
    
def get_publication(request,id = None):
    if id == None:
        return HttpResponse("Mal ID")
    publicacion = get_publication_by_id(id)
    for a in publicacion.archivos.all():
        print(a.archivo.url)
    return render(request, 'G_publication_page/get_publication.html', context={'publicacion': publicacion})
    
    