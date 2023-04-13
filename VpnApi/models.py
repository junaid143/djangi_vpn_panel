from django.db import models

# Create your models here.


# Open Vpn Panel

class VpnModel(models.Model):
    hostname = models.CharField(max_length=100)
    countryshort = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    config = models.TextField()
    is_enable = models.BooleanField(default=True)


