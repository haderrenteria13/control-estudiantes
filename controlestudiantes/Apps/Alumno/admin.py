from django.contrib import admin
from Apps.Alumno.models import EstudiantePrimaria, EstudianteSecundaria

# Register your models here.
admin.site.register(EstudiantePrimaria) # Registramos el modelo EstudiantePrimaria en el administrador de Django
admin.site.register(EstudianteSecundaria) # Registramos el modelo EstudianteSecundaria en el administrador de Django