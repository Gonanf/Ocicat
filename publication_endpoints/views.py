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

def get_publications_with_filter(filter,recent,data = None):
    order = 'id'
    if recent:
        order = '-id'
    if filter == "category":
            publicacion = PUBLICACION.objects.filter(categoria__nombre__in=[data]).order_by(order)
    elif filter == "autors":
            publicacion = PUBLICACION.objects.filter(autor = data).order_by(order)
    elif filter == "title":
            publicacion = PUBLICACION.objects.filter(titulo = data).order_by(order)
    elif filter == "any":
            publicacion = PUBLICACION.objects.all().order_by(order)
    else: publicacion = None
    return publicacion


def publication(request):
    if (request.method == "POST"):
        user = find_user(request)
        if (isinstance(user,HttpResponseNotFound)):
            return user
        portada = request.FILES.get('portada')
        if portada == None: return HttpResponseNotFound("BAD FIELD")
        temp_portada = MEDIA(archivo = portada)
        temp_portada.save()
        titulo = request.POST.get('titulo', None)
        if titulo == None: return HttpResponseNotFound("BAD FIELD")
        descripcion = request.POST.get('descripcion', None)
        if descripcion == None: return HttpResponseNotFound("BAD FIELD")

        publicacion = PUBLICACION(titulo = titulo,
                                  descripcion = descripcion,
                                  autor = user,
                                  portada = temp_portada)
        if request.POST.get('categorias',None) == None: return HttpResponseNotFound("BAD FIELD")
        if request.FILES.getlist('archivos[]', None) == None: return HttpResponseNotFound("BAD FIELD")
        if len(request.FILES.getlist('archivos[]')) == 0: return HttpResponseNotFound("BAD FIELD")
        publicacion.save()
        for cat in request.POST.get('categorias',None).split(','):
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
        
    
def publication_delete(request):
    print(request.POST.get('id',None))
    id = request.POST.get('id',None)
    if id == None: return HttpResponseNotFound("BAD ID")
    publicacion = get_publication_by_id(id)
    for i in publicacion.archivos.all():
        i.delete()
    publicacion.archivos.clear()
    publicacion.portada.delete()
    publicacion.delete()
    return HttpResponse("Eliminado con exito")
