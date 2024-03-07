from django.urls import path
from AppProject.views import *

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('empleados/', empleados, name='Empleados'),
    path('autores/', autores, name='Autores'),
    path('libros/', libros, name='Libros'),
    path('busqueda/', busqueda, name='Busqueda'),
    path('resultado/', resultado, name='Resultado'),
]
