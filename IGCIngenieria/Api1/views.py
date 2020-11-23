from django.shortcuts import render

from rest_framework import  status
from rest_framework import viewsets
from Api1 import serializer
from formulario.models import ListaPrecio
from .serializer import ProductoSerializer
# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
      serializer_class = ProductoSerializer
      queryset = ListaPrecio.objects.all()