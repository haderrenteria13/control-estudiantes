from django.db import models

class Alumno(models.Model):
    _nombre = models.CharField(max_length=150, blank=False)
    _apellido = models.CharField(max_length=150, blank=False)
    _edad = models.IntegerField(blank=False)
    _sexo = models.CharField(
        max_length=1,
        choices=[("M", "Masculino"), ("F", "Femenino")],
        blank=False,
    )
    _telefono = models.CharField(max_length=10, blank=True)
    _grado = models.CharField(
        max_length=10,
        blank=True,
        choices=[("1", "Primero"), ("2", "Segundo"), ("3", "Tercero"), ("4", "Cuarto"), ("5", "Quinto"), ("6", "Sexto"), ("7", "Séptimo"), ("8", "Octavo"), ("9", "Noveno"), ("10", "Décimo"), ("11", "Undécimo")],
    )

    _jornada = models.CharField(
        max_length=10,
        choices=[("mañana", "Mañana"), ("tarde", "Tarde")],
        blank=True,
    )
    _pae = models.BooleanField(
        default=False,                          
    )
    _transporte = models.BooleanField(
        default=False,  
    )

    class Meta:
        abstract = True

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, value):
        if not value:
            raise ValueError("El apellido no puede estar vacío")
        self._apellido = value

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        if value < 0:
            raise ValueError("La edad no puede ser negativa")
        self._edad = value

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, value):
        if value not in ["M", "F"]:
            raise ValueError("El sexo debe ser 'M' o 'F'")
        self._sexo = value

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, value):
        if not value.isdigit():
            raise ValueError("El teléfono debe contener solo números")
        self._telefono = value

    @property
    def grado(self):
        return self._grado

    @grado.setter
    def grado(self, value):
        self._grado = value

    @property
    def jornada(self):
        return self._jornada

    @jornada.setter
    def jornada(self, value):
        self._jornada = value

    @property
    def pae(self):
        return self._pae

    @pae.setter
    def pae(self, value):
        self._pae = value

    @property
    def transporte(self):
        return self._transporte

    @transporte.setter
    def transporte(self, value):
        self._transporte = value

    def obtener_informacion(self):
        return f"{self.nombre} {self.apellido}, {self.edad} años, {self.sexo}"

class EstudiantePrimaria(Alumno):
    etapa = models.CharField(
        max_length=10,
        choices=[("primaria", "Primaria")],
        default="primaria"
    )

    @staticmethod
    def es_primaria():
        return True

    @classmethod
    def crear_estudiante(cls, _nombre, _apellido, _edad, _sexo, _telefono, _grado, _jornada, _pae, _transporte):
        if _grado in ["1", "2", "3", "4", "5"]:
            return cls(
                _nombre=_nombre,
                _apellido=_apellido,
                _edad=_edad,
                _sexo=_sexo,
                _telefono=_telefono,
                _grado=_grado,
                _jornada=_jornada,
                _pae=_pae,
                _transporte=_transporte
            )
        else:
            raise ValueError("El grado no corresponde a un estudiante de primaria")

    def obtener_informacion(self):
        return f"{super().obtener_informacion()}, Grado: {self.grado}, Jornada: {self.jornada}"

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

    @staticmethod
    def es_secundaria():
        return True

    @classmethod
    def crear_estudiante(cls, _nombre, _apellido, _edad, _sexo, _telefono, _grado, _jornada, _pae, _transporte, media):
        if _grado in ["6", "7", "8", "9", "10", "11"]:
            return cls(
                _nombre=_nombre,
                _apellido=_apellido,
                _edad=_edad,
                _sexo=_sexo,
                _telefono=_telefono,
                _grado=_grado,
                _jornada=_jornada,
                _pae=_pae,
                _transporte=_transporte,
                media=media
            )
        else:
            raise ValueError("El grado no corresponde a un estudiante de secundaria")

    def obtener_informacion(self):
        return f"{super().obtener_informacion()}, Grado: {self.grado}, Jornada: {self.jornada}, Media: {self.media}"
