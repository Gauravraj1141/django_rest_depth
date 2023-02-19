from django.urls import path 
from rest_framework_nested import routers
from . import views

router  = routers.DefaultRouter()

router.register("pr",views.ProductViewset)
router.register('cart',views.GenerateCart)

cart_router = routers.NestedDefaultRouter(router , 'pr',lookup = 'product')
cart_router = routers.NestedDefaultRouter(router , 'cart',lookup = 'cart')

cart_router.register('addcart',views.CartItemViewset,basename='product-cart')
cart_router.register('items',views.CartItemViewset,basename='cart-item')

urlpatterns = router.urls + cart_router.urls