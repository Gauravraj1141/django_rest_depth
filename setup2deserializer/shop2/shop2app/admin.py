from django.contrib import admin

from .models  import Product  , Collection

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'unit_price', 'stock_quantity', 'collection',]
    


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['col_id', 'title', ]
    

 