from django.db import models

# Create your models here.
class Requet(models.Model):
    somme=models.IntegerField()
    duree=models.IntegerField()
    