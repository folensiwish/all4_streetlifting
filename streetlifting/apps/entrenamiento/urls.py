from django.urls import path
from . import views

urlpatterns = [
    path('', views.crear_entrenamiento, name='crear_entrenamiento')
]