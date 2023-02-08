from django.urls import path, include
from . import views
from . import class_base_view as myview


urlpatterns = [
    path("addprod", views.add_product, name="addprod"),
    path("updateprod/<int:id>/", views.update_prod, name="updateprod"),
    path("collection", views.mycollection, name="collection"),
    path("collection/<int:col_id>/", views.update_collection, name="udpatecol"),

]
         