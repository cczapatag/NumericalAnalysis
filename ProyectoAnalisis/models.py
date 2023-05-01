from django.db import models


class Funcion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    ecuacion = models.CharField(max_length=100)
