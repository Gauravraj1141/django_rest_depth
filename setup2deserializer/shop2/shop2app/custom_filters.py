from django_filters.rest_framework import FilterSet
from .models import Product

# here we can give custom filters with the help of djangofilter
class ProductFilterset(FilterSet):
    class Meta:
        model = Product
        fields = {
            'unit_price': ['gt', 'lt'],
            'collection': ['exact'],
            'stock_quantity':['gt'],
        }