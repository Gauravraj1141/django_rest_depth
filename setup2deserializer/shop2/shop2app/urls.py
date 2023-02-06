from django.urls import path, include
from . import views
urlpatterns = [
    path("addprod", views.AddProducts, name="addprod"),
    path("updateprod/<int:id>/", views.UpdateProd, name="updateprod"),
    path("collection", views.mycollection, name="collection"),
    path("collection/<int:col_id>/", views.updatecollection, name="udpatecol"),
    
]
