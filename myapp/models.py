from django.db import models

# Create your models here.
class Journey(models.Model):
    home = str
    room = int
    destination = str