from .models import Product ,  Collection , Review , CartItems , Cart
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','product_name', 'unit_price')

  
        
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = CartItems
        fields  = ('id', 'product', 'quantity','total_price')

    total_price = serializers.SerializerMethodField(method_name="price")

    def price(self,myitem:CartItems):
        return myitem.product.unit_price * myitem.quantity


    

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True , read_only=True)
    id = serializers.UUIDField(read_only = True)
    created_at = serializers.DateTimeField(read_only = True)

    total_price = serializers.SerializerMethodField()

    def get_total_price(self,cart):
        return sum([item.quantity * item.product.unit_price for item in cart.items.all()])
    class Meta:
        model = Cart
        fields = ['id','created_at' ,'items' , 'total_price']

# here we create new serializer for add product in cart 
class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    # here we need to override our save method because of our product adding in cart 
    # if any person gives wrong product id then add validation error in it 

    def validate_product_id(self,value):
        if not Product.objects.filter(pk  = value).exists():
            raise serializers.ValidationError(f"Product with id {value} does not exist".format(value))    
        return value

    def save(self, **kwargs):
        product_id  = self.validated_data['product_id']
        quantity = self.validated_data['quantity']
        cart_id = self.context['cart_id']
        
        try:
            # updating the quantity of our cart if it exist
            cart_item = CartItems.objects.get(cart_id=cart_id, product_id=product_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
        except :
            # create a new item
            self.instance = CartItems.objects.create(cart_id = cart_id , **self.validated_data)
        return self.instance
    class Meta:
        model = CartItems
        fields = ['id','product_id','quantity']


class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = ['quantity']