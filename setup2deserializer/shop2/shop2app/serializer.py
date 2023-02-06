from rest_framework import  serializers

from .models  import Product , Collection

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','product_name', 'unit_price', 'stock_quantity', 'collection',]
