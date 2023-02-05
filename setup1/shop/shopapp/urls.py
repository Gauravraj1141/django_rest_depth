from django.urls import path , include
from . import views


urlpatterns = [
    path("products/", views.Products, name="products"),
     path('__debug__/', include('debug_toolbar.urls')),
     path("collection/<int:pk>/",views.collection_detail, name = 'collection-detail')
]
