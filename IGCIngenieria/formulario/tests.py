from django.test import TestCase

# Create your tests here.
import json

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from django.utils import timezone



class PruebaUnitarias(TestCase):   
   
    # POST api
    def test_ingresarDatosAPI(self):
        fecha_hora = timezone.now()
        data= {"id":33,"Nombre":"Tablero Electrico","Valor":500000,
        "Descripcion":"Tablero para empresa CumbreDental","Estado":True,
        "Actualizacion" : fecha_hora} 
        response = self.client.post("/api/ListaPrecio/", data)
        self.assertEqual(response.status_code, 201)
    # GET api 
    def test_obtenerDatosAPI(self):      
        response = self.client.get("/api/ListaPrecio/")
        self.assertEqual(response.status_code, 200)
