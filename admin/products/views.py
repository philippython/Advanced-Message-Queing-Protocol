from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializer

# Create your views here.
class ProductViewSet(viewsets.ViewSet):
    def list(self, request): # api/products
        pass

    def create(self, request): #