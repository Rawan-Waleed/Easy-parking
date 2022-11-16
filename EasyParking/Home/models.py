from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Place(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city  = models.CharField(max_length=64)

class Add_Place(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=2048 , null=True)
    address = models.URLField(null=False , default="https://www.google.com/maps/")
    Price = models.CharField(max_length=2048)
    number_parking = models.IntegerField()

    days = models.CharField(max_length=64)

    open_time = models.TimeField()
    close_time = models.TimeField()

class User_Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parking_reserve = models.CharField(max_length=64 , null=True)
    hours = models.CharField(max_length=64  , null=True)
    day = models.CharField(max_length=64 , null=True)
    start_time = models.TimeField( null=True)
    end_time = models.TimeField( null=True)


