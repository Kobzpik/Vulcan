from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#if we want to view record data we have to look auth_user database in mysql
class User(AbstractUser):
    is_driver = models.BooleanField(default=False)
    is_officer = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    driver_license_No = models.CharField(max_length=20)

class Officer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)