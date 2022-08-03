from django.shortcuts import render

from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from familia.models import Familia

def inicio (request):
    datos = {"mensaje": "Esta es mi familia"}
    plantilla = loader.get_template("index.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)

def mama (request):
    datos = {"nombre": "Ines", "edad": 54, "nacimiento": "10-11-1967"}
    plantilla = loader.get_template("mama.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)

def papa (request):
    datos = {"nombre": "Guillermo", "edad": 55, "nacimiento": "30-04-1966" }
    plantilla = loader.get_template("papa.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)

def hija (request):
    datos = {"nombre": "Amparo", "edad": 9, "nacimiento": "07-06-2013" }
    plantilla = loader.get_template("hija.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)

def novio (request):
    datos = {"nombre": "Pablo", "edad": 37, "nacimiento": "01-09-1984" }
    plantilla = loader.get_template("novio.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)
