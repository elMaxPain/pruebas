from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def holaDjango(request):
    return HttpResponse("<h1>Hola Django!</h1>")

def pepe(request):
    return HttpResponse('Hola Pepe!')

def holaTu(request, nombre):
    return HttpResponse(f'Hola {nombre.capitalize()}! 😁')
