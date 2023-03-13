from django.urls import path , include
from . import  views

from django.urls import path 
from rest_framework import routers

router  = routers.DefaultRouter()

router.register("customer",views.CreateCustomer)



urlpatterns = router.urls 
# urlpatterns = [
#     path('shop',views.MyShop.as_view()),
# ]