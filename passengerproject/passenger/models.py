from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Passenger(models.Model):
    firstname=models.CharField(primary_key=True,max_length=20)
    lastname=models.CharField(max_length=20)
    travelpoints=models.DecimalField(max_digits=10,decimal_places=3)

    def __str__(self):
       return  self.firstname+self.lastname+self.travelpoints