from django.forms import ModelForm
from .models import Alummno # Importamos el modelo Alumno

class AlumnoForm(ModelForm): # Clase que representa el formulario Alumno
    class Meta:
        model = Alummno # Especificamos el modelo Alumno
        fields = '__all__' # Especificamos que campos queremos mostrar en el formulario

        