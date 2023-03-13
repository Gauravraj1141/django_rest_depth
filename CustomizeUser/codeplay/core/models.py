from django.db import models

# inherit abstactuser class in custom user
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)    