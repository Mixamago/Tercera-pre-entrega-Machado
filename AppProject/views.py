from django.shortcuts import render
from django.http import HttpResponse
from AppProject.models import *

# Create your views here.

#def inicio(request):
#    return render(request, 'AppProject/inicio.html')

def inicio(request):
        return render(request, 'AppProject/inicio.html')

def empleados(request):
    if request.method == "POST":
         empleado = Empleado(nombre=request.POST["nombre"], apellido=request.POST["apellido"], edad=request.POST["edad"], pais=request.POST["pais"], cargo=request.POST["cargo"], tarifa=request.POST["tarifa"])
         empleado.save()
         return render(request, "AppProject/inicio.html")
    return render(request, 'AppProject/empleados.html')

def autores(request):
    if request.method == "POST":
         autor = Autor(nombre=request.POST["nombre"], apellido=request.POST["apellido"], edad=request.POST["edad"], correo=request.POST["correo"], cantidad_libros=request.POST["libros"])
         autor.save()
         return render(request, "AppProject/inicio.html")
    return render(request, 'AppProject/autores.html')

def libros(request):
    if request.method == "POST":
         libro = Libro(titulo=request.POST["titulo"], autor=request.POST["autor"], paginas=request.POST["paginas"], genero=request.POST["genero"], ventas=request.POST["ventas"])
         libro.save()
         return render(request, "AppProject/inicio.html")
    return render(request, 'AppProject/libros.html')

def busqueda(request):
     return render(request, 'AppProject/busqueda.html')

def resultado(request):
     if request.GET["buscar"]:
          buscar = request.GET['buscar']
          objetivos = Empleado.objects.filter(nombre__icontains=buscar)
          exito = True
          return render(request, 'AppProject/resultadoBusqueda.html', {"nombre":buscar, "objetivos":objetivos, "exito":exito})
     else:
          exito = False
          return render(request, 'AppProject/resultadoBusqueda.html', {"exito":exito})