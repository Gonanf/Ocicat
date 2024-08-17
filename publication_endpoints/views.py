from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import Publication_Data
from models.models import MEDIA, PUBLICACION, CATEGORIA
from login_endpoints.views import find_user

def get_publication_by_id(id):
    try: publicacion = PUBLICACION.objects.get(pk = id)
    except PUBLICACION.DoesNotExist:
        publicacion = None
    if publicacion == None:
        return HttpResponse("La publicacion no existe")
    return publicacion

# Create your views here.
def publication(request):
    if (request.method == "POST"):
        user = find_user(request)
        if (user is HttpResponseNotFound):
            return user
        portada = request.FILES.get('portada')
        temp_portada = MEDIA(archivo = portada)
        temp_portada.save()
        publicacion = PUBLICACION(titulo = request.POST.get('titulo','NULL'),
                                  descripcion = request.POST.get('descripcion','NULL'),
                                  autor = user,
                                  portada = temp_portada)
        publicacion.save()
        for cat in request.POST.get('categorias','NULL').split(','):
            try: cat_found = CATEGORIA.objects.get(nombre = cat)
            except CATEGORIA.DoesNotExist:
                cat_found = None
                continue
            if cat_found != None:
                publicacion.categoria.add(cat_found)
        
        archivos = request.FILES.getlist('archivos[]')

        archivos_media = list()
        for files in archivos:
            temp = MEDIA(archivo = files)
            temp.save()
            publicacion.archivos.add(temp)
            archivos_media.append(temp.archivo.url)
        print(archivos_media)
        return HttpResponseRedirect("/publication_page/view/"+str(publicacion.pk))
    if request.method == "GET":
        id = request.GET.get('id', None)
        if id == None:
            return HttpResponse("Mal ID")
        publicacion = get_publication_by_id(id)
        return JsonResponse({
            'titulo': publicacion.titulo,
            'descripcion': publicacion.descripcion,
            'autor': publicacion.autor,
            'fecha': publicacion.fecha,
            'categorias': publicacion.categoria,
            'portada': publicacion.portada,
            'archivos': publicacion.archivos,
        })
    
    
