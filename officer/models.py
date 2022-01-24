from xml.parsers.expat import model
from django.db import models

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


class Fine(models.Model):
    id=models.AutoField(primary_key=True)
    driver_Name = models.CharField(max_length=50)
    vehicle_No = models.CharField(max_length=50)
    driver_license_No = models.CharField(max_length=124)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True)
    Police_station = models.CharField(max_length=130)
    Issuing_officer_ID = models.CharField(max_length=20)

    def __str__(self):
        return self.driver_Name