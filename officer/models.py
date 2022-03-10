from pickle import TRUE
from sqlite3 import Date
from xml.parsers.expat import model
from django.db import models
#from sqlalchemy import true
from authenticate.models import Driver,User
from datetime import date,time
import datetime
 
# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Location(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Offence(models.Model):
    offence = models.CharField(max_length=40)
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.offence
    
#class DriverName(models.Model):
    #user = models.ForeignKey(Driver, on_delete=models.CASCADE, primary_key = True)
    
    def __int__(self):
        return self.user     

class Fine(models.Model):
    id=models.AutoField(primary_key=True)
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True,null=True,limit_choices_to={'is_driver':True})
    vehicle_No = models.CharField(max_length=50)
    driver_license_No = models.CharField(max_length=124)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True)
    Nature_of_Offence = models.ForeignKey(Offence, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField(default=date.today)
    time = models.TimeField(default=datetime.datetime.now()) 
    Police_station = models.CharField(max_length=130)
    Issuing_officer_Name= models.CharField(max_length=20)

    def __str__(self):
        return self.id