from django.db import models


class Promotion(models.Model):
    description = models.CharField(max_length=444)
    discount = models.FloatField()


class Product(models.Model):
    title = models.CharField(max_length=444)
    descrption = models.CharField(max_length=444)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    slug = models.SlugField()
    listed_at = models.DateField(auto_now_add=True)
    inventory = models.IntegerField()
    # if our depend class is not upper of this child class then we give it in string we give our class below this
    collection = models.ForeignKey('Collection', on_delete=models.PROTECT)
    promotion = models.ManyToManyField(Promotion)


class Collection(models.Model):
    title = models.CharField(max_length=444)


class Customer(models.Model):
    # we should give choices in upper case
    # we should give B S and g in seperate variable because it is a good practice when we delte anyone then we delte it both places in defalut and in this also
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD = "G"
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, "BRONZE"),
        (MEMBERSHIP_SILVER, "SILVER"),
        (MEMBERSHIP_GOLD, "GOLD"),
    ]

    first_name = models.CharField(max_length=222)
    last_name = models.CharField(max_length=222)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=44)
    date_of_birth = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)


class Address(models.Model):
    street = models.CharField(max_length=444)
    city = models.CharField(max_length=444)
    customer = models.ForeignKey(
        Customer, related_name='address', on_delete=models.CASCADE)
    zip = models.IntegerField()


class Order(models.Model):
    PAYMENT_PENDING = "P"
    PAYMENT_COMPLETED = "C"
    PAYMENT_FAILED = "F"
    PAYMENT_COICES = [
        (PAYMENT_PENDING, "Pending"),
        (PAYMENT_COMPLETED, "Completed"),
        (PAYMENT_FAILED, "Failed"),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_COICES, default=PAYMENT_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
