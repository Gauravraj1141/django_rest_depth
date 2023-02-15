from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shopapp.serializer import ProductSerializer, CollectionSerializer
from shopapp.models import Product, Collection

# here we deserialize our serializer for giving values in it


@api_view(['GET', 'POST'])
def AddProducts(request):
    if request.method == "GET":
        data = Product.objects.select_related('collection').all()
        dictdata = CollectionSerializer(
            data, many=True)
        return Response(dictdata.data)

    elif request.method == "POST":  
        adddata = CollectionSerializer(data = request.data)
        # it will raise a exception automatically 
        adddata.is_valid()
        print(adddata)
        adddata.save()
        return Response("success fully added")
