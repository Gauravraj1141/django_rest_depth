from rest_framework import serializers
from .models import Product, Collection
from decimal import Decimal

# here we can create new serializer for colleciton class


class CollectionSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=33)
    title = serializers.CharField(max_length=34)



class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=33)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    # here we use this method but here it return so many query from the database it is a lengthy approach
    # here collection field is present in our Product model class with a foreignkey realtion
    # here it returns a id of collect
    # collection = serializers.PrimaryKeyRelatedField(
    #     queryset=Collection.objects.all())

    # if we want to show the collection name then we should use stringrelated field
    # it will query for each collection from the database if we don't give select_related() in our views when we fetch the product data from database
    # collection = serializers.StringRelatedField()

    # instead of it we can here collection serializers for showing colleciton values
# it is a nested serializer method
    # collection = CollectionSerializer()

    # instead of these we can use hyperlink method also and create a view and urls for it
    collection = serializers.HyperlinkedIdentityField(
        view_name='collection-detail',

    )



# here we use modelserializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # it is a good practice write all the fields name here instead of __all__ 
        # here we change the name of price as product_price
        fields = ['title', 'descrption', 'product_price','discount', 'discount_price',
                  'slug', 'listed_at', 'inventory', 'collection', 'promotion']

    # if we want to change the name of any field or add a new field then we should use  above method that we use simple serializer
    product_price = serializers.DecimalField(
        max_digits=8, decimal_places=2, source="price")

    # we can add new field also in it
    discount_price = serializers.SerializerMethodField(
        method_name='calculated_price')
    discount = serializers.SerializerMethodField(
        method_name='discount_p')

    def calculated_price(self, product: Product):
        return str(product.price - product.price*Decimal(.15))
     
    def discount_p(self,product:Product):
        return "15 %"
