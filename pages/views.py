import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models.models import CATEGORIA, PUBLICACION
from login_endpoints.views import find_user, USUARIO
from other_endpoints.views import categoria, get_autors, get_categories
from publication_endpoints.views import get_publication_by_id, get_publications_with_filter

def index(request):
    user = find_user(request)
    if isinstance(user,HttpResponseNotFound):
        user = None
    publicaciones = get_publications_with_filter("any", True)
    categorias = get_categories()
    autores = get_autors()
    return render(request,'main_page/index.html',context={'usuario': user,'publicaciones': publicaciones, 'categorias': categorias, 'autores': autores})

def login(request):
    return render(request,'login_page/login.html')

#TODO: Cambiar esto a un endpoint
def publications_with_filter(request,cant,type,filter,order):
    print(type)
    if order == "recent": publicacion = get_publications_with_filter(type,True,filter)[5*(cant-1):5 + (5*(cant - 1))]
    else: publicacion = get_publications_with_filter(type,False,filter)[5*cant:5 + (5*(cant - 1))]
    return render(request,'filter_page/filter.html',context= {'publications': publicacion})

def publication(request, type, id = None):
    usuario = find_user(request)
    if (type == "new"):
        if (isinstance(usuario,HttpResponseNotFound)):
            return usuario    
        categorias = get_categories()
        autores = get_autors()
        return render(request,'P_publication_page/post_publication.html', context={'categorias': categorias, 'autores': autores, 'usuario': usuario})
    if (type == "view"):
        if (isinstance(usuario,HttpResponseNotFound)):
            usuario = None
        if id == None:
            return HttpResponse("Mal ID")
        publicacion = get_publication_by_id(id)
        if publicacion == HttpResponse:
            return publicacion    
        categorias = get_categories()
        autores = get_autors()
        return render(request, 'G_publication_page/get_publication.html', context={'publicacion': publicacion,'categorias': categorias, 'autores': autores, 'usuario': usuario})
    

    
    