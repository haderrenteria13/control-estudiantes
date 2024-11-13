from django.shortcuts import render, redirect
from .models import Alummno # Importamos el modelo Alumno

# Create your views here.
def inicio(request): # Función que representa la vista inicio
    alumno = Alummno.objects.all() # Consultamos todos los alumnos
    context = {
        'valumno': alumno # Enviamos los alumnos a la plantilla
    }
    return render(request, 'Alumno/inicio.html', context) # Retornamos la plantilla inicio.html con los alumnos

def alumno_new(request): 
    if request.method == 'POST':
        alumno_form = AlumnoForm(request.POST)
        if alumno_form.is_valid():
            alumno_form.save()
            return redirect ('inicio')
    else:
        alumno_form = AlumnoForm()
    return render(request, 'Alumno/alumno_form.html', {'alumno_form': alumno_form})

def alumno_update(request, id): 
    alummno = get_object_or_404(Alummno, id=id)
    if request.method == 'POST':
        alumno_form = AlumnoForm(request.POST, instance=alummno)
        if alumno_form.is_valid():
            alumno_form.save()
            return redirect ('inicio')
    else:
        alumno_form = AlumnoForm(instance=alummno)
    return render(request, 'Alumno/alumno_form.html', {'alumno_form': alumno_form})
