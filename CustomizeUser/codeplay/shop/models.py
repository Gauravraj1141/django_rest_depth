from django.db import models
from django.conf import settings

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class PaymentStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_type = models.CharField(max_length=44)

class Order(models.Model):
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.ForeignKey(PaymentStatus , on_delete= models.CASCADE)
    customer = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete= models.CASCADE)

    class Meta:
        permissions = {
            ('cancel_order' , 'Can Cancel Order')
        }

class OrderItem(models.Model):
    order = models.ForeignKey(Order , on_delete= models.PROTECT)
    product = models.ForeignKey(Products , on_delete= models.CASCADE , related_name='order_items')
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=10,decimal_places=2)

class Customer(models.Model):
    phone = models.CharField(max_length= 200)
    birth_date = models.DateField(null=True , blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"