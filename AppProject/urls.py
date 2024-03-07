from django.urls import path
from AppProject.views import *

urlpatterns = [
    path('', inicio),
    path('empleados/', empleados),
    path('autores/', autores),
    path('libros/', libros),
]
