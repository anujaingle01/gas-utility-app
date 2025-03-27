from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('csr', 'Customer Support Representative'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='customer')
