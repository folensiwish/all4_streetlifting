from django.shortcuts import render

# Create your views here.

def crear_entrenamiento(request):
    return render(request, 'entrenamiento/crear_entrenamiento.html', context={})