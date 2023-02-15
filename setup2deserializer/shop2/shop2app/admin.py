from django.contrib import admin

from .models  import Product  , Collection , Review

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'unit_price', 'stock_quantity', 'collection',]
    


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['col_id', 'title', ]
    

 

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'description', 'date', )
    

 