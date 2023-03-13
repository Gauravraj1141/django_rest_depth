from django.contrib import admin
from .models import  Products , OrderItem , Order , PaymentStatus , Customer

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display =  ('name', 'price', 'description', 'created_at', )

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'unit_price', )
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display =  ('placed_at', 'payment_status', 'customer', )
    

@admin.register(PaymentStatus)
class PaymentStatusAdmin(admin.ModelAdmin):
    list_display =  ('status_id', 'status_type', )

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display =  ('id','user_id','phone','birth_date' )
    

