from .models import Product, Collection
from .serializer import ProductSerializer , ICollectionSerializer 
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.db.models import Count

# here we repeat the code for get and post and another is put petch and delete so alternate is viewset it will take all those functions inside it 
from rest_framework.viewsets import  ReadOnlyModelViewSet  , ModelViewSet

# only this ProductViewset class will handle get post put patch delte 
class ProductViewset(ModelViewSet):
    # if we don't want to give any logic in it then we should use only these simple terms 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_field = "id"


    
class MyCollectionViewset(ModelViewSet):
    queryset = Collection.objects.annotate(product_count = Count('product_collection')).all()   
    serializer_class = ICollectionSerializer
    lookup_field = "col_id"

    