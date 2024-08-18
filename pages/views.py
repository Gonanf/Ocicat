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

#TODO: Cambiar esto a un endpoint
def publications_with_filter(request,cant,type,filter,order):
    if type == "category":
        if order == "recent":
            try: publicacion = PUBLICACION.objects.filter(categoria__nombre__in=[filter]).order_by('-id')[cant-5:cant]
            except PUBLICACION.DoesNotExist:
                publicacion = None
        else:
            try: publicacion = PUBLICACION.objects.filter(categoria__nombre__in=[filter]).order_by('id')[cant-5:cant]
            except PUBLICACION.DoesNotExist:
                publicacion = None
        
    if type == "autors":
        if order == "recent":
            try: publicacion = PUBLICACION.objects.filter(autor = filter).order_by('-id')[cant-5:cant]
            except PUBLICACION.DoesNotExist:
                publicacion = None
        else:
            try: publicacion = PUBLICACION.objects.filter(autor = filter).order_by('id')[cant-5:cant]
            except PUBLICACION.DoesNotExist:
                publicacion = None
    if type == "title":
        if order == "recent":
            try: publicacion = PUBLICACION.objects.filter(titulo = filter).order_by('-id')[cant-5:cant]
            except PUBLICACION.DoesNotExist:
                publicacion = None
        else:
            try: publicacion = PUBLICACION.objects.filter(titulo = filter).order_by('id')[cant-5:cant]
            except PUBLICACION.DoesNotExist:
                publicacion = None
    if publicacion == None:
        return HttpResponse("La publicacion no existe")
    return render(request,'filter_page/filter.html',context= {'publications': publicacion})

def publication(request, type, id = None):
    if (type == "new"):
        usuario = find_user(request)
        if (isinstance(usuario,HttpResponseNotFound)):
            return usuario
        return render(request,'P_publication_page/post_publication.html', context={'categorias': [categoria.nombre for categoria in CATEGORIA.objects.all()], 'usuario': usuario.nombre})
    if (type == "view"):
        if id == None:
            return HttpResponse("Mal ID")
        publicacion = get_publication_by_id(id)
        if publicacion == HttpResponse:
            return publicacion    
        return render(request, 'G_publication_page/get_publication.html', context={'publicacion': publicacion})
    

    
    