from django.db import models

class Sessions(models.TextChoices):
    USER = 'user', 'user'
    PLACE_OWNER = 'po', 'place_owner'
    BAND_OWNER = 'bo', 'band_owner'

class Users(models.Model):
    email = models.EmailField(max_length=80)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)
    session = models.CharField(choices=Sessions.choices, default=Sessions.USER)

    def __str__(self):
        return self.name
