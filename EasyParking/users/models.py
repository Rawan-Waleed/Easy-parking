from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = PhoneField(null=False, blank=False, unique=True)
    is_owner = models.BooleanField(default=False)