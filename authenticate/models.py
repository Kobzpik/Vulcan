from django.db import models
from django.contrib.auth.models import AbstractUser
import random

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

#codes class for OTP authentication
class Codes(models.Model):
    number = models.CharField(max_length=5 , blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key = True)
 
    def __str__(self):
        return str(self.number)
    
    def save(self, *args, **kwargs):
        number_lsit = [x for x in range(10)]
        code_items = []

        for i in range(5):
            num = random.choice(number_lsit)
            code_items.append(num)
        
        code_string = "".join(str(item) for item in code_items)
        self.number = code_string
        super().save(*args , ** kwargs)