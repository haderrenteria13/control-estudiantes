from django import forms
from .models import EstudiantePrimaria, EstudianteSecundaria
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AlumnoForm(forms.ModelForm):
    TIPO_ALUMNO_CHOICES = [
        ('primaria', 'Primaria'),
        ('secundaria', 'Secundaria'),
    ]
    tipo_alumno = forms.ChoiceField(choices=TIPO_ALUMNO_CHOICES, required=True, widget=forms.HiddenInput())
    media = forms.BooleanField(required=False, help_text="Indica si el estudiante está en media académica (grados 10 y 11)")

    class Meta:
        model = EstudiantePrimaria  # Usamos EstudiantePrimaria como modelo base
        fields = '__all__'
        exclude = ['etapa']  # Excluir el campo etapa

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['media'].widget.attrs.update({'class': 'field-media'})
        self.fields['_grado'].widget.attrs.update({'class': 'field-grado'})
        if self.instance and self.instance.pk:
            if isinstance(self.instance, EstudianteSecundaria):
                self.fields['media'].initial = self.instance.media
            else:
                self.fields.pop('media')

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']