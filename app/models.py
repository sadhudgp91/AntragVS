"""
Definition of models.
"""

from django.db import models


# Create your models here.

class Post(models.Model):
    sapname= models.TextField()
    vorname= models.TextField()

class grunddaten(models.Model):
    sapkonto= models.TextField()
    vorname= models.TextField()

