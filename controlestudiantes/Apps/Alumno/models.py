from django.db import models

class Alumno(models.Model):  # Clase base para todos los estudiantes
    nombre = models.CharField(max_length=150, blank=False, default='nombre')
    apellido = models.CharField(max_length=150, blank=False, default='Apellido')  # Agrega un valor predeterminado
    edad = models.IntegerField(blank=False, default=6)  
    sexo = models.CharField(
        max_length=1,
        choices=[("M", "Masculino"), ("F", "Femenino")],
        blank=False,
        default="M"
    )
    telefono = models.CharField(max_length=10, blank=True, default='0000000000')
    grado = models.CharField(max_length=10, blank=True, default='1')
    jornada = models.CharField(
        max_length=10,
        choices=[("mañana", "Mañana"), ("tarde", "Tarde")],
        blank=True,
        default="mañana"
    )
    pae = models.BooleanField(default=False)
    transporte = models.BooleanField(default=False)
    etapa = models.CharField(max_length=10, blank=True)

    class Meta:
        abstract = True  # No se creará una tabla para esta clase

class EstudiantePrimaria(Alumno):
    etapa = models.CharField(
        max_length=10,
        choices=[("primaria", "Primaria")],
        default="primaria"
    )

class EstudianteSecundaria(Alumno):
    etapa = models.CharField(
        max_length=10,
        choices=[("secundaria", "Secundaria")],
        default="secundaria"
    )
    media = models.BooleanField(
        default=False, 
        help_text="Indica si el estudiante está en media académica (grados 10 y 11)"
    )
