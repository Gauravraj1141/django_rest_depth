from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProductSerializer
from .models import Product

@api_view()
def Products(request):
    data = Product.objects.all()
    print(data)
    dictdata = ProductSerializer(data, many = True)
    print(dictdata.data)
    return Response(dictdata.data)
