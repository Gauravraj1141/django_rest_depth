from rest_framework import serializers
from .models import Product, Collection


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'unit_price',
                  'stock_quantity', 'collection', ]


class ICollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['col_id', 'title', 'product_count']

    # here we should give  readonly true because when we post req then it will throw and error
    product_count = serializers.IntegerField(read_only=True)
