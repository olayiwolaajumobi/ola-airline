from django.db import models
from django.utils.text import slugify
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile_img = models.FileField(upload_to="profiles", blank=True)


class FlightLocation(models.Model):
    code= models.CharField(max_length=3)
    location= models.CharField(max_length=250)

class Booking(models.Model):
    flight = models.ForeignKey(FlightLocation, on_delete=models.CASCADE)
    passanger_name = models.CharField(max_length=100)
    passanger_email = models.EmailField()
    form= models.CharField(max_length=200)
    paid = models.BooleanField(default=False)