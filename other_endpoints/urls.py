from django.urls import path, include
from . import views
urlpatterns = [
    path('categoria',views.categoria, name='categoria')
]
