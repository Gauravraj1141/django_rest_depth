from django.shortcuts import render, HttpResponse
from rest_framework.renderers import JSONRenderer
from .serializers import DogSerializer
from .models import Dogs ,  DogsBreed
import json
from rest_framework.decorators import api_view
from rest_framework.views  import APIView
from rest_framework.response import Response
from rest_framework.status  import HTTP_201_CREATED , HTTP_204_NO_CONTENT



@api_view()
def AllDogs(request):
    all_dogs = Dogs.objects.all()
    serializerdog = DogSerializer(all_dogs,many=True)
    return Response(serializerdog.data)

class MyDog(APIView):
    def get(self , request,pk):
        all_dogs = Dogs.objects.filter(id=pk)
        serializerdog = DogSerializer(all_dogs,many=True)
        return Response(serializerdog.data)
    
    def post(self,request,pk):
        breed_id = request.data.get('breed')
        print(request.data)
        breed = DogsBreed.objects.get(breed=breed_id)
        data = DogSerializer(data=request.data)
        if data.is_valid():
            data.save(breed = breed)
            return Response(data.data , status=HTTP_201_CREATED)
        return Response(data.data,status=HTTP_204_NO_CONTENT)
       