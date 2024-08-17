from django.urls import path, include
from . import views
urlpatterns = [
    path('publication',views.publication, name='publicacion_end')
]
