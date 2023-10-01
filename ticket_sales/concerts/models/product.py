from django.db import models
from .users import Users
from .place import Place

class ProductType(models.TextChoices):
    TICKET = 'tk', 'Ticket'

class Product(models.Model):
    type = models.CharField(max_length=2, choices=ProductType.choices, default=ProductType.TICKET)
    price=models.DecimalField(decimal_places=2,max_digits=10)
    userId=models.ForeignKey(Users, on_delete=models.CASCADE)
    placeId=models.ForeignKey(Place, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type
