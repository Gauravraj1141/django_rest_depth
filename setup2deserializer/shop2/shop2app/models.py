from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=44)
    unit_price = models.DecimalField(max_digits=4,decimal_places=2)
    stock_quantity = models.IntegerField()
    collection =  models.ForeignKey("Collection", on_delete=models.CASCADE)


class Collection(models.Model):
    col_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=444)