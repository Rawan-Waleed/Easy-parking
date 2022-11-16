from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Place(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    city_choose = models.TextChoices("city", ["Riyadh", "Jeddah", "Abha" , "Makkah" ,"Al-Medina" , "Al-Dammam"])
    city  = models.CharField(max_length=64, choices = city_choose.choices , default=city_choose.Riyadh)

class Add(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=2048 , default=None)
    address = models.URLField(null=False , default="https://www.google.com/maps/")
    Price = models.CharField(max_length=2048)
    number_parking = models.IntegerField()

    opening_days = models.TextChoices("days", ["Saturday", "Sunday", "Monday" , "Tuesday" ,"Al-Wednesday" , "Al-Thursday" , "Friday"])
    days = models.CharField(max_length=64, choices = opening_days.choices , default=opening_days.Saturday)

    open_time = models.TimeField()
    close_time = models.TimeField()
