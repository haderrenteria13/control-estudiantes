from django import forms
from .models import EstudiantePrimaria, EstudianteSecundaria

class AlumnoForm(forms.ModelForm):
    TIPO_ALUMNO_CHOICES = [
        ('primaria', 'Primaria'),
        ('secundaria', 'Secundaria'),
    ]
    tipo_alumno = forms.ChoiceField(choices=TIPO_ALUMNO_CHOICES, required=True, widget=forms.HiddenInput())
    media = forms.BooleanField(required=False, help_text="Indica si el estudiante está en media académica.")
    tipo_de_media = forms.CharField(required=False, help_text="Nombre de la media en la cual está estudiando, si aplica.")
    
    class Meta:
        model = EstudiantePrimaria  # Usamos EstudiantePrimaria como modelo base
        fields = '__all__'
        exclude = ['etapa']  # Excluir el campo etapa

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['media'].widget.attrs.update({'class': 'field-media'})
        self.fields['_grado'].widget.attrs.update({'class': 'field-grado'})
        self.fields['tipo_de_media'].widget.attrs.update({'class': 'field-tipo-de-media'})
        if self.instance and self.instance.pk:
            if isinstance(self.instance, EstudianteSecundaria):
                self.fields['media'].initial = self.instance.media
                self.fields['tipo_de_media'].initial = self.instance.tipo_de_media
            else:
                self.fields.pop('media')
                self.fields.pop('tipo_de_media')

    def clean(self):
        cleaned_data = super().clean()
        media = cleaned_data.get("media")
        tipo_de_media = cleaned_data.get("tipo_de_media")

        if media and not tipo_de_media:
            self.add_error('tipo_de_media', 'Este campo es obligatorio si el estudiante está en media académica.')

        return cleaned_data