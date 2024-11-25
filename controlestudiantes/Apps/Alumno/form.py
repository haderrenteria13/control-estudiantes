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
    media = forms.BooleanField(required=False, help_text="Indica si el estudiante está en media académica (grados 10 y 11)")

    class Meta:
        model = EstudiantePrimaria  # Usamos EstudiantePrimaria como modelo base
        fields = '__all__'
        exclude = ['etapa']  # Excluir el campo etapa

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['tipo_alumno'].widget = forms.HiddenInput()
            if isinstance(self.instance, EstudianteSecundaria):
                self.fields['media'].initial = self.instance.media
            else:
                self.fields.pop('media')

    def clean(self):
        cleaned_data = super().clean()
        edad = cleaned_data.get("edad")
        telefono = cleaned_data.get("telefono")
        grado = cleaned_data.get("grado")

        # Validación personalizada para la edad
        if edad and edad < 5:
            self.add_error('edad', "La edad debe ser mayor o igual a 5 años.")

        # Validación personalizada para el teléfono
        if telefono and not telefono.isdigit():
            self.add_error('telefono', "El teléfono debe contener solo números.")

        if grado and not grado.isdigit():
            self.add_error('grado', "El grado debe contener solo números.")

        return cleaned_data

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']