from django.urls import path
from .views import (
    inicio, 
    loginView,
    registro,
    logoutVista,
    #HomeUsuario,
    jugar,
    tablero,
    resultado_pregunta
    )

urlpatterns = [
    path('', inicio, name='inicio'),
    #path('HomeUsuario/', HomeUsuario, name='HomeUsuario'),
    path('registro/', registro, name='registro'),
    path('login/', loginView, name='login'),
    path('logoutVista/', logoutVista, name='logoutVista'),
    path('tablero/', tablero, name='tablero'),
    path('jugar/', jugar, name='jugar'),
    path('resultado/int<int:pregunta_respondida_pk>/', resultado_pregunta, name='resultado')
]

