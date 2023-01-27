from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED,HTTP_200_OK, HTTP_202_ACCEPTED, HTTP_204_NO_CONTENT
from .serializers import ProductSerializer
from .models import Products, User
import random

# Create your views here.
class ProductViewSet(viewsets.ViewSet):
    def list(self, request): # /api/products
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request): # /api/products
        serializer =  ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, HTTP_201_CREATED)
        return Response("Invalid error", 404)

    def retrieve(self, request, pk=None): # /api/products/<str:id>
        product = Products.objects.get(id=pk)
        serializer = ProductSerializer(data=product)
        return Response(serializer.data, HTTP_200_OK)

    def update(self, request, pk=None) : # /api/products/<str:id>
        product = Products.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None) : # /api/products/<str:id>
        product = Products.objects.get(id=pk)
        product.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })