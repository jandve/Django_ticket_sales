from django.db import models
from users import Users
from place import Place

class Product_type(models.TextChoices):
    TICKET = 'tk', 'Ticket'

class Product(models.Model):
    type = models.CharField(max_length=2,choices=Product_type.choices, default=Product_type.TICKET)
    price=models.DecimalField(decimal_places=2,max_digits=10)
    userid=models.ForeignKey(Users)
    placeid=models.ForeignKey(Place)
 
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)