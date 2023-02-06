from django.shortcuts import render
from .models import Product, Collection
from rest_framework.decorators import api_view
from .serializer import ProductSerializer
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
def AddProducts(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        # here we can show what it our data generate that we give input
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'PATCH','DELETE'])
def UpdateProd(request, id):
    proddata = get_object_or_404(Product, id=id)
    if request.method == "GET":
        serializer = ProductSerializer(proddata)
        return Response(serializer.data)
# here we update a particualr fiedls
    elif request.method == "PUT":
        serializer = ProductSerializer(proddata, data=request.data)
        serializer.is_valid(raise_exception=True)
        # print(serializer.data)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

        # in the patch method we can give a single attribute of our field and change that particular it saves bandwidth of our server 
    elif request.method == "PATCH":
        serializer = ProductSerializer(
            proddata, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        proddata.delete()
        return Response({"Deleted":"Successfully Deleted"} ,status=status.HTTP_204_NO_CONTENT)
    
