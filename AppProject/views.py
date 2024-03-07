from django.shortcuts import render
from django.http import HttpResponse
from AppProject.models import *

# Create your views here.

#def inicio(request):
#    return render(request, 'AppProject/inicio.html')

def inicio(request):
        return render(request, 'AppProject/inicio.html')

def empleados(request):
    return render(request, 'AppProject/empleados.html')

def autores(request):
    return render(request, 'AppProject/autores.html')

def libros(request):
    return render(request, 'AppProject/libros.html')