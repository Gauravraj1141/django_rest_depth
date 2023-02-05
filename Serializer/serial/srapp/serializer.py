from rest_framework import serializers
from .models import ProductTrali, Collection
# here we give some field of our model here we give field by own


# we create one more serializer for collect
class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    stock_quantitiy = serializers.IntegerField()


class ProductsSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    # and we can rename our field name so how it works see  below
    Product = serializers.CharField(max_length=343, source="product_name")
    # here we show price in decimal so it will show us in string so we can change it in to string we add "COERCE_DECIMAL_TO_STRING" : FALSE IN SETTINGS.PY
    product_price = serializers.DecimalField(max_digits=8, decimal_places=2)

    # we can give new field here with the help of these field and make a calculation also
    # we give serializermethodfields

    product_discounted_price = serializers.SerializerMethodField(
        method_name="Calc_discount")

    # here we annotate it give this model name here
    def Calc_discount(self, product: ProductTrali):
        return product.product_price - product.product_price*.15

    # in it we can add one more models fields
    #  here we give related field name that we give in collection's pr_name
    collection = CollectionSerializer()
