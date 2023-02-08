from django.shortcuts import render
from .models import Product, Collection
from .serializer import ProductSerializer , ICollectionSerializer 
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework.views import APIView

from rest_framework.generics import mixins

class AddProduct(APIView):
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = ProductSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# # for adding , deleting , updating product data 

class UpdateProd(APIView):
    def get(self,request , id):
        proddata = get_object_or_404(Product, id=id)    
        serializer = ProductSerializer(proddata)
        return Response(serializer.data)

    def put(self,request,id): 
        proddata = get_object_or_404(Product, id=id)    
        serializer = ProductSerializer(proddata, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self,request,id): 
        proddata = get_object_or_404(Product, id=id)    
        serializer = ProductSerializer(proddata, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self,request,id): 
        proddata = get_object_or_404(Product, id=id)    
        proddata.delete()
        return Response({"Deleted":"Successfully Deleted"} ,status=status.HTTP_204_NO_CONTENT)
    


# for collection update delete and get and add data for collection 

class MyCollection(APIView):
    def get(self,request):
        coldata = Collection.objects.annotate(product_count = Count('product_collection')).all()
        serializer = ICollectionSerializer(coldata, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = ICollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)




class UpdateCollection(APIView):

    def get(self,request,col_id):
        coldetail = get_object_or_404(Collection.objects.annotate(product_count = Count("product_collection")),col_id = col_id)
        serializer = ICollectionSerializer(coldetail )
        return Response(serializer.data , status=status.HTTP_200_OK)

    def put(self,request,col_id):
        coldetail = get_object_or_404(Collection.objects.annotate(product_count = Count("product_collection")),col_id = col_id)
        serializer = ICollectionSerializer(coldetail,data = request.data )
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        return Response(serializer.data , status=status.HTTP_201_CREATED)

    def patch(self,request,col_id):
        coldetail = get_object_or_404(Collection.objects.annotate(product_count = Count("product_collection")),col_id = col_id)
        serializer = ICollectionSerializer(coldetail,data = request.data ,partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        return Response(serializer.data , status=status.HTTP_201_CREATED)

    def delete(self,request,col_id):
        coldetail = get_object_or_404(Collection.objects.annotate(product_count = Count("product_collection")),col_id = col_id)
        coldetail.delete()
        return Response( status=status.HTTP_204_NO_CONTENT)



