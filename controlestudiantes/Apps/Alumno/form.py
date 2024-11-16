from django import forms
from .models import EstudiantePrimaria, EstudianteSecundaria
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AlumnoForm(forms.ModelForm):
    TIPO_ALUMNO_CHOICES = [
        ('primaria', 'Primaria'),
        ('secundaria', 'Secundaria'),
    ]
    tipo_alumno = forms.ChoiceField(choices=TIPO_ALUMNO_CHOICES, required=True)

    class Meta:
        model = EstudiantePrimaria  # Usamos EstudiantePrimaria como modelo base
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        edad = cleaned_data.get("edad")
        telefono = cleaned_data.get("telefono")

        # Validación personalizada para la edad
        if edad and edad < 5:
            self.add_error('edad', "La edad debe ser mayor o igual a 5 años.")

        # Validación personalizada para el teléfono
        if telefono and not telefono.isdigit():
            self.add_error('telefono', "El teléfono debe contener solo números.")

        return cleaned_data

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']