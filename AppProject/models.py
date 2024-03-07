from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    edad = models.IntegerField
    pais = models.CharField(max_length=15)
    cargo = models.CharField(max_length=15)
    tarifa = models.IntegerField

class Libro(models.Model):
    titulo = models.CharField(max_length=15)
    autor = models.CharField(max_length=15)
    paginas = models.IntegerField
    genero = models.CharField(max_length=15)
    ventas = models.IntegerField

class Autor(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    edad = models.IntegerField
    correo = models.EmailField
    cantidad_libros = models.IntegerField