from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('login_page',views.login, name='login_page'),
]
