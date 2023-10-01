# Create your models here.
from django.db import models

class User(models.Model):
    name=models.CharField(max_length=100,unique=True, help_text="Enter your name")
    lastName=models.CharField(max_length=1002,unique=True, help_text="Enter your lastname")
    email=models.CharField(max_length=1002,unique=True, help_text="Enter your email")
    password=models.CharField(max_length=1002,unique=True)
    session_rol=[
('user', 'normal_user'),
('admin', 'administrator'),
('band', 'ban_manager'),
('place', 'place_manager'),
]
    roles = models.CharField(max_length=20, choices=session_rol, default='user')
    def __str__(self):
        return self.name

class Band(models.Model):
    name=models.CharField(max_length=100,unique=True, help_text="Enter your band name")
    gender=models.CharField(max_length=20,unique=True)
    rate=models.DecimalField(decimal_places=2,max_digits=10)
    userId=models.ForeignKey(User, on_delete= models.CASCADE)
    def __str__(self):
        return self.name

class Place(models.Model):
    name=models.CharField(max_length=100,unique=True, help_text="Enter your place name")
    address=models.CharField(max_length=50,unique=True)
    phone=models.PositiveIntegerField(max_digits=8)
    gain=models.FloatField()
    capacity=models.FloatField()
    userId=models.ForeignKey(User, on_delete= models.CASCADE)
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=100,unique=True, help_text="Enter your place name")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    userId=models.ForeignKey(User, on_delete= models.CASCADE)
    bandId=models.ForeignKey(User, on_delete= models.CASCADE)
    placeId=models.ForeignKey(User, on_delete= models.CASCADE)
    def __str__(self):
        return self.name   

    disponible=models.BooleanField(blank=True,default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
