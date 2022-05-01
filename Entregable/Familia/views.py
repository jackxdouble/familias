from http.client import HTTPResponse
from operator import imod
from django.shortcuts import render

from django.template import loader

from Familia.models import Familia

def familia(self):

    familiar1 = Familia (nombre = 'Jennifer', edad = 28, cumple = '1993-01-25')

    familiar1.save()

    familiar2 = Familia (nombre = 'Joyce', edad = 30, cumple = '1992-01-09')

    familiar2.save()

    familiar3 = Familia (nombre = 'Jeremy', edad = 31, cumple = '1991-01-07')

    familiar3.save()

    diccionario  = {
        '1nombre':familiar1.nombre,
        '1edad':familiar1.edad,
        '1cumple':familiar1.cumple,
        '2nombre':familiar2.nombre,
        '2edad':familiar2.edad,
        '2cumple':familiar2.cumple,
        '3nombre':familiar3.nombre,
        '3edad':familiar3.edad,
        '3cumple':familiar3.cumple,   
    }

    plantilla  = loader.get_template('familia.HTML')

    documento = plantilla.render(diccionario)

    return HTTPResponse(documento)

    