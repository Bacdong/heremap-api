from django.db import models
from django.db.models.aggregates import Count
from random import randint

# Create your models here.
class Address(models.Model):
    apartment_number = models.CharField(max_length = 40)
    street = models.CharField(max_length = 40)
    ward = models.CharField(max_length = 40)
    district = models.CharField(max_length = 40)
    city = models.CharField(max_length = 40)

    def __str__(self):
        return self.city 


class APIKey(models.Model):
    key = models.CharField(max_length = 200)
    status = models.BooleanField(default = True)

    def __str__(self):
        return self.key
