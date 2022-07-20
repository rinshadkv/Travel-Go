from pyexpat import model
from unicodedata import name
from django.db import models

from host.models import Rooms


# Create your models here.
class User(models.Model):
    password=models.CharField(max_length=12)
    email=models.CharField(max_length=100)
    name=models.CharField(max_length=25,default="")
    class Meta:
        db_table='user_tb'

class Booking(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE) 
    room_id=models.ForeignKey(Rooms,on_delete=models.CASCADE)
    email=models.CharField(max_length=100)    
    name=models.CharField(max_length=25) 
    check_in=models.DateField()  
    check_out=models.DateField()
    


class Payment(models.Model):
    booking_id=models.ForeignKey(Booking,on_delete=models.CASCADE)
    price=models.IntegerField()
    payment_mode=models.CharField(max_length=20)
    payment_status=models.CharField(max_length=20)

