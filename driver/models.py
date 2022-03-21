from django.db import models
from authenticate.models import User
from officer.models import Fine
from datetime import date,time
import datetime

# Create your models here.
class Payment(models.Model):
    id=models.AutoField(primary_key=True)
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True,null=True,limit_choices_to={'is_driver':True})
    fine = models.ForeignKey(Fine, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField(default=date.today)
    time = models.TimeField(default=datetime.datetime.now()) 
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    paid = models.BooleanField(default="False")
    

#complain form
class Complain(models.Model):
    id=models.AutoField(primary_key=True)
    date = models.DateField(default=date.today)
    complainer_name = models.CharField(max_length=30 ,blank=True,null=True)
    email = models.CharField(max_length=30 ,blank=True,null=True)
    complain = models.CharField(max_length=500 )

