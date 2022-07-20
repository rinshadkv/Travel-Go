from distutils.command.upload import upload
from email.mime import image
from operator import mod
from unicodedata import name
from .services import *

from django.db import models

# Create your models here.

class Property(models.Model):
    property_name=models.CharField(max_length=25)
    country=models.CharField(max_length=25)
    countrycode=models.CharField(max_length=5)
    phone=models.BigIntegerField()
    place=models.CharField(max_length=40)
    property_type=models.CharField(max_length=30)
    image=models.ImageField(upload_to=change_path)

    class Meta:
        db_table='property'

class Account(models.Model):
    email=models.CharField(max_length=100,default="")
    password=models.CharField(max_length=12)
    property_id=models.ForeignKey(Property,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
   
    class Meta:
        db_table='accounts'






class Rooms(models.Model):
    property_id = models.ForeignKey(Property,on_delete=models.CASCADE)
    room_number=models.IntegerField()
    room_name=models.CharField(max_length=20)
    adult=models.IntegerField()
    child=models.IntegerField()
    price=models.FloatField()
    beds=models.IntegerField()
    status=models.BooleanField(default=False)

    class Meta:
        db_table='rooms'


class property_images(models.Model):
    
    property_id=models.ForeignKey(Property,on_delete=models.CASCADE)

    property_image=models.ImageField(upload_to=hotel_path)
    type=models.CharField(max_length=20,default="")
    

    class Meta:
        db_table='property_images'

class AddAmenities(models.Model):
    property_id=models.ForeignKey(Property,on_delete=models.CASCADE)
    amenities=models.CharField(max_length=1000)  

    class Meta:
        db_table='amenities' 

class AboutProperty(models.Model):
    property_id=models.ForeignKey(Property,on_delete=models.CASCADE)
    description=models.TextField(default="")
    rules=models.TextField(default="")

    class Meta:
        db_table="about_property"



   