from django.urls import path, include

from . import viewset_views as myview
# now we use nested router for our review so now we are not using rest_framework 's router '
# from rest_framework.routers import DefaultRouter

# here we import our drf nested router 
from rest_framework_nested import routers

# we can print our route 
from pprint import pprint

# it is parent routers 
router = routers.DefaultRouter()
router.register("product",myview.ProductViewset)
router.register("collection",myview.MyCollectionViewset)

# here we create child routers
# routers.NestedDefaultRouter(parent_route,'parent prefix name',lookup = 'product')
products_router = routers.NestedDefaultRouter(router,'product',lookup = 'product')

# here we need to register our child router 
products_router.register('reviews',myview.MyReiewsViewset , basename='product-reviews')



# it will generate all urls 
router.urls

# here we can print our routes 
# pprint(router.urls)
urlpatterns =router.urls + products_router.urls
# pprint(urlpatterns)