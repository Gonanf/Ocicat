from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('login_page',views.login, name='login_page'),
    path('publication_page/<str:type>',views.publication, name='publicacion_pagina'),
    path('publication_page/view/<int:id>', views.get_publication, name="obtener_publicacion"),
]
