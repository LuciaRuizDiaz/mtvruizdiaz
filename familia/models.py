from django.shortcuts import render
from django.db import models



class Familia(models.Model):
    nombre = models.CharField(max_length=45)
    edad = models.IntegerField()
    nacimiento = models.DateField()

# Create your models here.
