from django.urls import path, include

from . import generic_views as myview


urlpatterns = [
    path("addproduct/",myview.AddProduct.as_view(),name="addproduct"),
    path("update/<int:id>/", myview.UpdateProd.as_view(), name="update"),
    path("mycollection/", myview.MyCollection.as_view(), name="mycollection"),
    path("mycollection/<int:col_id>/", myview.UpdateCollection.as_view(), name="mycollection"),

]
         