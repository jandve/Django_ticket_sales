from django.db import models
from .user import User
from .validators import validate_capacity

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    gain = models.FloatField()
    capacity = models.IntegerField(validators=[validate_capacity,])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

