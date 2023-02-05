from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=33)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
