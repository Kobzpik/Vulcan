from sqlite3 import Date
from xml.parsers.expat import model
from django.db import models
from authenticate.models import Driver

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

    def __str__(self):
        return self.offence
    
class DriverName(models.Model):
    user = models.ForeignKey(Driver, on_delete=models.CASCADE, primary_key = True) 
    
    def __int__(self):
        return self.user      

class Fine(models.Model):
    id=models.AutoField(primary_key=True)
    driver_Name = models.ForeignKey(DriverName, on_delete=models.SET_NULL, blank=True, null=True)
    vehicle_No = models.CharField(max_length=50)
    driver_license_No = models.CharField(max_length=124)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True)
    Nature_of_Offence = models.ForeignKey(Offence, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField()
    time = models.TimeField() 
    Police_station = models.CharField(max_length=130)
    Issuing_officer_Name= models.CharField(max_length=20)

    def __str__(self):
        return self.driver_Name