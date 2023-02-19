from django.contrib import admin

from .models import Product, Collection , Review , Cart , CartItems


admin.site.register(Product)
admin.site.register(Collection)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(CartItems)

