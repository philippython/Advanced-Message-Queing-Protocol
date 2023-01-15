from django.shortcuts import render
from rest_framework import viewsets, response
from .serializers import ProductSerializer
from .models import Products

# Create your views here.
class ProductViewSet(viewsets.ViewSet):
    def list(self, request): # /api/products
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        if serializer.is_valid:
            response.  Response(serializer.data)

    def create(self, request): # /api/products
        pass

    def retrieve(self, request, pk=None): # /api/products/<str:id>
        pass

    def update(self, request, pk=None) : # /api/products/<str:id>
        pass

    def destroy(self, request, pk=None) : # /api/products/<str:id>
        pass