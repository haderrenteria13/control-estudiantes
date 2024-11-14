from django.db import models

# Create your models here.
class Alummno (models.Model): # Clase que representa el modelo Alumno
    nombre = models.CharField(max_length=150, blank=False) 
    apellido = models.CharField(max_length=150, blank=False) 
    edad = models.IntegerField(blank=False)  
    sexo = models.CharField(max_length=1, blank=False) 
    
    
    def __str__(self): # Método que retorna el nombre y apellido del alumno
        return self.nombre + ' ' + self.apellido + ' ' + str(self.edad) + ' ' + self.sexo # Retornamos el nombre y apellido del alumno