from .models import Product, Collection
from .serializer import ProductSerializer , ICollectionSerializer 
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework.views import APIView


# we can see this generic file and see all the classes and methods in these 
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView

# in this ListCreateAPIView we can show all products as well as we can create a post request 
class AddProduct(ListCreateAPIView):
    ''' 
    # if we don't want to give any logic in it then we should use only these simple terms 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    '''

    
    # if we want to give some logic in our queryset and serializer then we should use these functions also 
    def get_queryset(self):
        queryset = Product.objects.all()
        # here we write our logic 
        return queryset
    
    # here we return our serializer_class 
    def get_serializer_class(self):
        return ProductSerializer

    # if we want to give some context data in our serilizer then we should use it 
    def get_serializer_context(self):
        return {"request":self.request}
    


# #RetrieveUpdateDestroyAPIView is for adding , deleting , put and patch product data 
class UpdateProd(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # here we override pk with id in our url 
    lookup_field = "id"

    # and here we override delete method because we give some extra pram in it 
    # so it works properly 
    def delete(self,request,id): 
        proddata = get_object_or_404(Product, id=id)    
        proddata.delete()
        return Response({"Deleted":"Successfully Deleted"} ,status=status.HTTP_204_NO_CONTENT)
    


# for collection update delete and get and add data for collection 

class MyCollection(ListCreateAPIView):
    # so here we add some logic in queryset so that the reason we give here get_queryset 
    def get_queryset(self):
        queryset = Collection.objects.annotate(product_count = Count('product_collection')).all()
        return queryset
    def get_serializer_class(self):
        return ICollectionSerializer
  

class UpdateCollection(RetrieveUpdateDestroyAPIView):
    lookup_field  = "col_id"
    queryset = Collection.objects.annotate(product_count = Count("product_collection"))
    serializer_class = ICollectionSerializer
