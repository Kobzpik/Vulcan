from django.db import models
from authenticate.models import User
from datetime import date,time
import datetime

# Create your models here.
class Payment(models.Model):
    id=models.AutoField(primary_key=True)
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True,null=True,limit_choices_to={'is_driver':True})
    date = models.DateField(default=date.today)
    time = models.TimeField(default=datetime.datetime.now()) 
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    

