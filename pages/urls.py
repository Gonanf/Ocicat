from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('login_page',views.login, name='login_page'),
    path('publication_page/<str:type>',views.publication, name='publicacion_pagina'),
    path('publication_page/<str:type>/<int:id>', views.publication, name="obtener_publicacion"),
    path('publication_page/filter/<int:cant>/<str:type>/<str:filter>/<str:order>', views.publications_with_filter, name="obtener_publicacion_filtro"),
    
]
