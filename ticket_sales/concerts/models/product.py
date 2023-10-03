from django.db import models
from .user import User
from .band import Band
from .place import Place
from .validators import validate_price

class ProductType(models.TextChoices):
    TICKET = 'tk', 'Ticket'

class Product(models.Model):
    type = models.CharField(max_length=2, choices=ProductType.choices, default=ProductType.TICKET)
    price=models.DecimalField(decimal_places=2,max_digits=10,validators=[validate_price,])
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    place=models.ForeignKey(Place, on_delete=models.CASCADE)
    band=models.ForeignKey(Band, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type
