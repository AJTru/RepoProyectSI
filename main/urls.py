from django.urls import path
from . import views

from .views import VRegistro

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.iniciar_sesion, name='login'),
    path('registro/', VRegistro.as_view(), name="registro"),
    path('catalogo/', views.catalogo, name="catalogo"),
    

]
