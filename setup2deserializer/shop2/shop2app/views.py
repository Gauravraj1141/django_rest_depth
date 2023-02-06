from django.shortcuts import render
from .models import Product, Collection
from rest_framework.decorators import api_view
from .serializer import ProductSerializer , CollectionSerializer
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.db.models import Count


@api_view(['GET', 'POST'])
def add_product(request):
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

# for adding , deleting , updating product data 

@api_view(['GET', 'PUT', 'PATCH','DELETE'])
def update_prod(request, id):
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
    


# for collection update delete and get and add data for collection 
@api_view(['GET','POST'])
def mycollection(request):
    if request.method  == 'GET':
        coldata = Collection.objects.annotate(product_count = Count('product_collection')).all()
        serializer = CollectionSerializer(coldata, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method  == 'POST':
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)




@api_view(['GET','PUT','PATCH','DELETE'])
def update_collection(request, col_id):
    coldetail = get_object_or_404(Collection.objects.annotate(product_count = Count("product_collection")),col_id = col_id)

    if request.method  == 'GET':
        serializer = CollectionSerializer(coldetail )
        return Response(serializer.data , status=status.HTTP_200_OK)

    if request.method  == 'PUT':
        serializer = CollectionSerializer(coldetail,data = request.data )
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        return Response(serializer.data , status=status.HTTP_201_CREATED)
    elif request.method  == 'PATCH':
        serializer = CollectionSerializer(coldetail,data = request.data ,partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        return Response(serializer.data , status=status.HTTP_201_CREATED)
    elif request.method  == 'DELETE':
        coldetail.delete()
        return Response(  status=status.HTTP_204_NO_CONTENT)

