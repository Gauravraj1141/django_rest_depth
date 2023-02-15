from rest_framework import serializers
from .models import Product, Collection , Review


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


# reviews serializer 

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','name','description','date' ]

    def create(self, validated_data):
        product_id = self.context['product_id']
        product_instance = Product.objects.get(id  = product_id)
        return Review.objects.create(product=product_instance , **validated_data)
