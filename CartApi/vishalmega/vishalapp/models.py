from django.db import models
from uuid import uuid4
from django.core.validators import MaxValueValidator, MinValueValidator

class Product(models.Model):
    product_name = models.CharField(max_length=44)
    unit_price = models.DecimalField(max_digits=10,decimal_places=2)
    stock_quantity = models.IntegerField()
    collection =  models.ForeignKey("Collection", on_delete=models.CASCADE , related_name="product_collection")


class Collection(models.Model):
    col_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=444)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name='review')
    name = models.CharField(max_length=333)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)


class Cart(models.Model):
    id = models.UUIDField(primary_key=True , default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItems(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE , related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(
        validators= [MinValueValidator(1)]
    )

    class Meta:
        unique_together = [['cart','product']]