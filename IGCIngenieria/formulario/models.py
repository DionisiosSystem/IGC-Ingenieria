from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime



class Usuario(models.Model):
        Nombre=models.CharField(max_length=50,null=True)
        Apellido=models.CharField(max_length=50,null=True)
        Email=models.CharField(max_length=50,null=True)



        def __str__(self): # metodo que se llama
            return 'Nombre :%s , Apellido :%s , Email :%s ' % (self.Nombre, self.Apellido, self.Email)

class Contacto(models.Model):
        Nombre = models.CharField(max_length=50,null=True)
        Apellido = models.CharField(max_length=50,null=True)
        Email= models.CharField(max_length=50,null=True)
        Telefono= models.CharField(max_length=50,null=True)
        Mensaje= models.CharField(max_length=300,null=True)
        #Fecha= models.DateField(),auto_now_add=True, blank=False)
        Fecha = models.DateTimeField(default=datetime.now(), blank=True)
        Estado = models.BooleanField(default=True)

        def __str__(self):  # metodo que se llama
            return 'Nombre :%s , Apellido :%s , Email :%s , Telefono :%s , Mensaje :%s , Fecha :%s'%(self.Nombre,self.Apellido,self.Email,self.Telefono,self.Mensaje,self.Fecha)




class ListaPrecio(models.Model):
        Nombre = models.CharField(max_length=50,null=True)
        Valor = models.CharField(max_length=50,null=True)
        Descripcion = models.CharField(max_length=50,null=True)
        Estado = models.BooleanField(default=True)
        Actualizacion = models.DateTimeField(default=datetime.now(), blank=True)


        def __str__(self):  # metodo que se llama
            return 'Nombre :%s , Valor :%s , Descripcion :%s , Estado :%s , Actualizacion :%s' % (self.Nombre, self.Valor, self.Descripcion, self.Estado, self.Actualizacion)


