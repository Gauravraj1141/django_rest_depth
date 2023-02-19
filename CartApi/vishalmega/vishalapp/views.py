from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet , GenericViewSet
from .models import Product ,CartItems , Cart
from .serializer import  ProductSerializer , CartItemSerializer , CartSerializer , AddCartItemSerializer , UpdateCartItemSerializer
from rest_framework.mixins import CreateModelMixin , RetrieveModelMixin , DestroyModelMixin

class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    
class CartItemViewset(ModelViewSet):
    # here we can allow all the methods name which we allow for this endpoint 
    # so only these button will show on front 
    http_method_names = ['get','post','patch','delete']

    # queryset = CartItems.objects.all()
    # serializer_class= CartItemSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddCartItemSerializer
        elif self.request.method == "PATCH":
            return UpdateCartItemSerializer
        return CartItemSerializer 

    def get_queryset(self):
        # here we give our cart uuid's filter and give select related means it is foreign key so we get these product in one query not a seperates 
        queryset = CartItems.objects.filter(cart_id = self.kwargs['cart_pk']).select_related('product')
        return queryset

    # here we send the cartid in our serializer where we add products in our cart 
    def get_serializer_context(self):
        return {"cart_id":self.kwargs['cart_pk']}
    


class GenerateCart(CreateModelMixin,GenericViewSet,RetrieveModelMixin ,DestroyModelMixin):
    # here we prefetch all the product of this particular  cart in one time not seperately it will reduce the bandwidth of our db
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = CartSerializer
    

