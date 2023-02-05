from django.db import models


class ProductTrali(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=444)
    product_catagory = models.CharField(max_length=455)
    product_price = models.IntegerField()
    product_discount = models.DecimalField(
        default=4.23, max_digits=4, decimal_places=2)
    product_desc = models.CharField(max_length=444)

    def __str__(self):
        return self.product_name


class Collection(models.Model):
    stock_quantitiy = models.IntegerField(default=3)
    pr_name = models.ForeignKey(
        ProductTrali, on_delete=models.CASCADE, related_name="collection")

    def __str__(self):
        return self.stock_quantitiy
