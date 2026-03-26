from django.db import models
from django.utils import timezone # Importante para manejar zonas horarias
# Create your models here.

class Ejercicio(models.Model):
    nombre_ejercicio = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nombre_ejercicio

class Sesion(models.Model):
    fecha_sesion = models.DateField(default=timezone.now)
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Sesion - {self.fecha_sesion}'

class Serie(models.Model):
    sesion = models.ForeignKey(Sesion, on_delete=models.CASCADE)
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)

    repeticion = models.PositiveSmallIntegerField()
    peso_lastre = models.DecimalField(max_digits=5, decimal_places=2)
    rpe = models.PositiveSmallIntegerField() #rpe es la escala de esfuerzo de la serie 
    rir = models.PositiveSmallIntegerField() #rir son las repeticiones en reserva estimadas antes de llegar al fallo

    def __str__(self):
        return f'{self.ejercicio.nombre_ejercicio} - {self.peso_lastre}kg'