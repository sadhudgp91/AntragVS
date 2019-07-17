

from django.db import models


# Create your models here.

class Post(models.Model):
    sapname= models.TextField()
    vorname= models.TextField()

class grunddaten(models.Model):
    sapname= models.TextField()
    vorname= models.TextField()
    nachname = models.TextField()
    instno = models.IntegerField()
    einrichtung = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    finanzstelle =models.TextField()
    GültigVon = models.TextField()
    GültigBis = models.TextField()
