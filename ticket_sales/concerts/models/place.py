from django.db import models

from ticket_sales.concerts.models.users import Users


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    gain = models.FloatField()
    capacity = models.IntegerField()
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
