from django.urls import path # Importamos la función path para mapear URLs
from . import views as v # Importamos las vistas de la aplicación Alumno

urlpatterns = [ # Lista de rutas de la aplicación Alumno
    path('', v.inicio, name='inicio'), # Ruta que llama a la vista inicio
]