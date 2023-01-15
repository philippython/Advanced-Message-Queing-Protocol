from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from .serializers import ProductSerializer
from .models import Products

# Create your views here.
class ProductViewSet(viewsets.ViewSet):
    def list(self, request): # /api/products
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request): # /api/products
        serializer =  ProductSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, HTTP_201_CREATED)
        return Response("Invalid error", 404)

    def retrieve(self, request, pk=None): # /api/products/<str:id>
        pass

    def update(self, request, pk=None) : # /api/products/<str:id>
        pass

    def destroy(self, request, pk=None) : # /api/products/<str:id>
        pass
