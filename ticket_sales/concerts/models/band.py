from django.db import models
from .user import User

class Genders(models.TextChoices):
    ROCK = 'rk', 'Rock'
    POP = 'po', 'Pop'
    JAZZ = 'jz', 'Jazz'

class Band(models.Model):
    name=models.CharField(max_length=100, help_text="Enter your band name")
    gender = models.CharField(max_length=2, choices=Genders.choices, default=Genders.ROCK)
    rate=models.DecimalField(decimal_places=2,max_digits=10)
    userId=models.ForeignKey(User, on_delete= models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    def _str_(self):
        return self.name
