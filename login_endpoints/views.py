from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseNotFound, JsonResponse
from .models import Login
from models.models import USUARIO

#TODO: Implementar UUID (Si se puede el V7 con la funcion de tiempo) y encriptar la cookie
def find_user(request):
    galletita = request.COOKIES.get('sesion')
    if galletita is None:
        return HttpResponseNotFound("No existe")
    try: user = USUARIO.objects.get(pk = galletita)
    except USUARIO.DoesNotExist:
        return HttpResponseNotFound("No existe")
    return user


def login_end(request):
    if request.method == "POST":
        data = Login(request.POST)
        if data.is_valid():
            try: user = USUARIO.objects.get(contrasena = data.cleaned_data['contrasena'], gmail = data.cleaned_data['gmail'])
            except USUARIO.DoesNotExist:
                return HttpResponseNotFound("No existe")
            response = HttpResponse("Logrado con exito")
            response.set_cookie('sesion', user.pk)
            return response
        return HttpResponseBadRequest("No es valido")
    if request.method == "GET":
        result = find_user(request)
        if (result is HttpResponseNotFound):
            return result
        return JsonResponse({"nombre": result.nombre})
    if request.method == "DELETE":
        galletita = request.COOKIES.get('sesion')
        if galletita is None:
            return HttpResponseNotFound("No existe")
        response = HttpResponse("Logrado")
        response.delete_cookie('sesion')
        return response
