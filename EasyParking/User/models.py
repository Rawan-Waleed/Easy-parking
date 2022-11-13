from django.db import models
from phone_field import PhoneField

# Create your models here.

class User(models.Model):
    email =models.EmailField()
    password = models.TextField()
    phone_number = PhoneField(null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=1024)
    last_name = models.CharField(max_length=1024)
    Gender = models.TextChoices("Gender", ["Male", "Female"])
    City = models.TextChoices("City", ["Riyadh", "Jeddah" , "Makkah" , "Abha", "Medina" , "Al-Dammam" ])
    Gender_Type  = models.CharField(max_length=64, choices = Gender.choices, default=Gender)
    City_choose = models.CharField

