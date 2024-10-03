from django.urls import path, include
from . import views
urlpatterns = [
    path('publication',views.publication, name='publicacion_end'),
    path('publication_delete',views.publication_delete, name='delete_publication')
]
