from rest_framework import serializers
from .models import EstudiantePrimaria, EstudianteSecundaria

class EstudiantePrimariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstudiantePrimaria
        fields = '__all__'

class EstudianteSecundariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstudianteSecundaria
        fields = '__all__'