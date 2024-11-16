from django.forms import ModelForm
from .models import Alummno # Importamos el modelo Alumno
from django.contrib.auth.forms import UserCreationForm # Importamos el formulario UserCreationForm
from django.contrib.auth.models import User # Importamos el modelo User

class AlumnoForm(ModelForm): # Clase que representa el formulario Alumno
    class Meta:
        model = Alummno # Especificamos el modelo Alumno
        fields = '__all__' # Especificamos que campos queremos mostrar en el formulario
class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']