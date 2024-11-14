from django.urls import path # Importamos la función path para mapear URLs
from . import views as v # Importamos las vistas de la aplicación Alumno

urlpatterns = [ # Lista de rutas de la aplicación Alumno
    path('', v.inicio, name='inicio'), # Ruta que llama a la vista inicio
    path('new', v.alumno_new, name='alumno_new'), # Ruta que llama a la vista alumno_new
    path('edit/<int:id>/', v.alumno_update, name='alumno_update'), # Ruta que llama a la vista alumno_update
    path('delete/<int:id>/', v.alumno_delete, name='alumno_delete'), # Ruta que llama a la vista alumno_delete
]