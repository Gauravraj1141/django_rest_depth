from django.urls import path, include
from . import views
urlpatterns = [
    path("addprod", views.AddProducts, name="addprod"),
    path("updateprod/<int:id>/", views.UpdateProd, name="updateprod"),
]
