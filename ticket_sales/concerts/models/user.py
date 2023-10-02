from django.db import models
from .validators import validate_password
from django.core.validators import EmailValidator

class Sessions(models.TextChoices):
    USER = 'user', 'user'
    PLACE_OWNER = 'po', 'place_owner'
    BAND_OWNER = 'bo', 'band_owner'

class User(models.Model):
    email = models.EmailField(max_length=80,validators=[EmailValidator('no es un mail valido')])
    password = models.CharField(max_length=20,validators=[validate_password,])
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)
    session = models.CharField(max_length=10, choices=Sessions.choices, default=Sessions.USER)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
