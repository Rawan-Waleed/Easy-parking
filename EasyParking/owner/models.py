from django.db import models
from phone_field import PhoneField

# Create your models here.

class User(models.Model):
    email =models.EmailField()
    password = models.TextField()
    phone_number = PhoneField(null=False, blank=False, unique=True)
    place_name = models.CharField(max_length=1024)
    City = models.TextChoices("City", ["Riyadh", "Jeddah" , "Makkah" , "Abha", "Medina" , "Al-Dammam" ])
    City_choose = models.CharField

