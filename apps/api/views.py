from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductoSerializer
from apps.Tienda.models import *
# Create your views here.



class ProductoViewSet(viewsets.ModelViewSet):
    queryset=Producto.objects.all()
    serializer_class = ProductoSerializer