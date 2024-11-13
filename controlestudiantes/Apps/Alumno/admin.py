from django.contrib import admin
from Apps.Alumno.models import Alummno # Importamos el modelo Alumno

# Register your models here.
admin.site.register(Alummno) # Registramos el modelo Alumno en el administrador de Django