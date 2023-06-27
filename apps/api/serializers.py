from rest_framework import serializers

from apps.Tienda.models import *



class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        models= Producto 
        fields = '__all__'



