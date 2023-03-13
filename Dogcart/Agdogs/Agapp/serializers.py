from .models import Dogs , DogsBreed
from rest_framework import serializers 

class DogSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=44)
    breed = serializers.CharField(max_length=44)
    age = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=13,decimal_places=2)

    def create(self,validated_data):
        return Dogs.objects.create(**validated_data)