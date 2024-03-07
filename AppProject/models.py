from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    edad = models.IntegerField(null=True, blank=True)
    pais = models.CharField(max_length=15)
    cargo = models.CharField(max_length=15)
    tarifa = models.IntegerField(null=True, blank=True)

class Autor(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    edad = models.IntegerField(null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    cantidad_libros = models.IntegerField(null=True, blank=True)

class Libro(models.Model):
    titulo = models.CharField(max_length=15)
    autor = models.CharField(max_length=15)
    paginas = models.IntegerField(null=True, blank=True)
    genero = models.CharField(max_length=15)
    ventas = models.IntegerField(null=True, blank=True)