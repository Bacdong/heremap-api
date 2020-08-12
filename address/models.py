from django.db import models
import requests
import json

# Create your models here.
class Address(models.Model):
    apartment_number = models.CharField(max_length = 40)
    street = models.CharField(max_length = 40)
    ward = models.CharField(max_length = 40)
    district = models.CharField(max_length = 40)
    city = models.CharField(max_length = 40)

    def __str__(self):
        return self.city 

