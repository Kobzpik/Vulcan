from django.db import models

# Create your models here.

class list(models.Model):
    Id=models.AutoField(primary_key=True)
    firstName= models.CharField(max_length=30)
    age=models.CharField(max_length=10)
    class Meta:
        db_table="beta"
    
    def __str__(self):
         return self.item
    

   