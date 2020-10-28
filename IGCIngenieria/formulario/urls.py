from django.contrib import admin
from django.urls import path
from formulario import views

urlpatterns = [
    path('index/', views.home, name="index"),
    path('contacto/', views.contacto, name="contacto"),
    path('listadoMensajes/', views.mensajes, name="mensajes"),


]