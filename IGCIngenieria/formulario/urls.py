from django.contrib import admin
from django.urls import path
from formulario import views
from django.contrib.auth.views import (logout_then_login, LoginView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView ,PasswordResetCompleteView)


urlpatterns = [
    path('index/', views.home, name="index"),
    path('contacto/', views.contacto, name="contacto"),
    path('listadoMensajes/', views.mensajes, name="listadoMensajes"),
    path('clientes/', views.clientes, name="clientes"),
    path('obrasCiviles/', views.obrasCiviles, name="obrasCiviles"),
    path('obrasMenores/', views.obrasMenores, name="obrasMenores"),
    path('QuienesSomos/', views.QuienesSomos, name="QuienesSomos"),

     path('listadoProductos/', views.productos, name="listadoProductos"),
    path('insertarProducto/', views.insertarProducto, name="insertarProducto"),
    path('delete/<int:producto_id>', views.delete, name="delete"),
]