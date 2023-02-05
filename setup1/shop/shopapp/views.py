from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProductSerializer , CollectionSerializer
from .models import Product  , Collection



@api_view()
def Products(request):
    data = Product.objects.select_related('collection').all()
    dictdata = ProductSerializer(data, many = True , context = {"request":request})
    
    return Response(dictdata.data)

# it is for colleciton hyperlink  

@api_view()
def collection_detail(request,pk):
    data = Collection.objects.all()
    dictdata = CollectionSerializer(data,many=True)

    return Response(dictdata.data)
