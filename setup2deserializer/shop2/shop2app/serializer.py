from rest_framework import  serializers

from .models  import Product , Collection

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','product_name', 'unit_price', 'stock_quantity', 'collection',]

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['col_id','title','product_count']

    product_count = serializers.IntegerField()

   