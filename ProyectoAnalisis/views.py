from django.shortcuts import render
from .models import Funcion


def lista_funciones(request):
    funciones = Funcion.objects.all()
    return render(request, 'lista_funciones.html', {'funciones': funciones})
