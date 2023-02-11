from django.urls import path, include

from . import viewset_views as myview
from rest_framework.routers import SimpleRouter
# we can print our route 
from pprint import pprint

router = SimpleRouter()
router.register("product",myview.ProductViewset)
router.register("collection",myview.MyCollectionViewset)
# it will generate all urls 
router.urls

# here we can print our routes 
# pprint(router.urls)
urlpatterns =router.urls