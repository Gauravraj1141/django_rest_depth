from django.db import models


class Notification(models.Model):
    name = models.CharField(max_length=44)
    email = models.EmailField()
