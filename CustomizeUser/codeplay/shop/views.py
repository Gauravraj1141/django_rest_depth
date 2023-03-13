from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import Customer
from .serializer import CustomerSerializer

# Create your views here.
class MyShop(APIView):
    def get(self,request):
        return Response("oky")
    
class CreateCustomer(CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer