from rest_framework import serializers
from formulario.models import ListaPrecio

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaPrecio
        fields ='__all__'