from django.db import models

# Create your models here.
from django.db import models


class directores(models.Model):
    nombre = models.TextField(max_length=100)
    edad = models.IntegerField()
    nacionalidad = models.TextField(max_length=50)

    def __str__(self):
        return self.nombre,


class peliculas(models.Model):
    titulo = models.TextField(max_length=50)
    anio = models.IntegerField()
    genero = models.TextField(max_length=50)
    director = models.ForeignKey(directores, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class sinopsis(models.Model):
    sinopsis = models.TextField(max_length=500)
    pelicula = models.ForeignKey(peliculas, on_delete=models.CASCADE)

    def __str__(self):
        return self.sinopsis
