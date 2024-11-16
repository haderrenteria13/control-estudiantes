from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import EstudiantePrimaria, EstudianteSecundaria
from .form import AlumnoForm
from django.db.models import Q

@login_required
def inicio(request):
    query = request.GET.get('q')
    if query:
        alumnos_primaria = EstudiantePrimaria.objects.filter(
            Q(nombre__icontains=query) | 
            Q(apellido__icontains=query) | 
            Q(edad__icontains=query) | 
            Q(sexo__icontains=query) | 
            Q(telefono__icontains=query)
        ).values('id', 'nombre', 'apellido', 'edad', 'sexo', 'telefono', 'grado', 'jornada', 'pae', 'transporte', 'etapa')
        alumnos_secundaria = EstudianteSecundaria.objects.filter(
            Q(nombre__icontains=query) | 
            Q(apellido__icontains=query) | 
            Q(edad__icontains=query) | 
            Q(sexo__icontains=query) | 
            Q(telefono__icontains=query)
        ).values('id', 'nombre', 'apellido', 'edad', 'sexo', 'telefono', 'grado', 'jornada', 'pae', 'transporte', 'etapa')
        alumnos = alumnos_primaria.union(alumnos_secundaria)
    else:
        alumnos_primaria = EstudiantePrimaria.objects.all().values('id', 'nombre', 'apellido', 'edad', 'sexo', 'telefono', 'grado', 'jornada', 'pae', 'transporte', 'etapa')
        alumnos_secundaria = EstudianteSecundaria.objects.all().values('id', 'nombre', 'apellido', 'edad', 'sexo', 'telefono', 'grado', 'jornada', 'pae', 'transporte', 'etapa')
        alumnos = alumnos_primaria.union(alumnos_secundaria)
    
    context = {
        'valumno': alumnos,
        'query': query,
    }
    return render(request, 'Alumno/inicio.html', context)

@login_required
def inicio_primaria(request):
    query = request.GET.get('q')
    if query:
        estudiantes_primaria = EstudiantePrimaria.objects.filter(
            Q(nombre__icontains=query) | 
            Q(apellido__icontains=query)
        )
    else:
        estudiantes_primaria = EstudiantePrimaria.objects.all()
    context = {
        'estudiantes_primaria': estudiantes_primaria,
        'query': query,
    }
    return render(request, 'Alumno/primaria.html', context)

@login_required
def inicio_secundaria(request):
    query = request.GET.get('q')
    if query:
        estudiantes_secundaria = EstudianteSecundaria.objects.filter(
            Q(nombre__icontains=query) | 
            Q(apellido__icontains=query)
        )
    else:
        estudiantes_secundaria = EstudianteSecundaria.objects.all()
    context = {
        'estudiantes_secundaria': estudiantes_secundaria,
        'query': query,
    }
    return render(request, 'Alumno/secundaria.html', context)

@login_required
def alumno_new(request):
    if request.method == 'POST':
        alumno_form = AlumnoForm(request.POST)
        if alumno_form.is_valid():
            tipo_alumno = alumno_form.cleaned_data.pop('tipo_alumno')
            if tipo_alumno == 'primaria':
                alumno = EstudiantePrimaria(**alumno_form.cleaned_data)
            else:
                alumno = EstudianteSecundaria(**alumno_form.cleaned_data)
            alumno.save()
            return redirect('inicio')
    else:
        alumno_form = AlumnoForm()
    return render(request, 'Alumno/alumno_form.html', {'alumno_form': alumno_form})

@login_required
def alumno_update(request, id):
    try:
        alumno = EstudiantePrimaria.objects.get(id=id)
        tipo_alumno = 'primaria'
    except EstudiantePrimaria.DoesNotExist:
        alumno = EstudianteSecundaria.objects.get(id=id)
        tipo_alumno = 'secundaria'

    if request.method == 'POST':
        alumno_form = AlumnoForm(request.POST, instance=alumno)
        if alumno_form.is_valid():
            alumno_form.save()
            return redirect('inicio')
    else:
        alumno_form = AlumnoForm(instance=alumno)
        alumno_form.fields['tipo_alumno'].initial = tipo_alumno
    return render(request, 'Alumno/alumno_form.html', {'alumno_form': alumno_form})

@login_required
def alumno_delete(request, id):
    try:
        alumno = EstudiantePrimaria.objects.get(id=id)
    except EstudiantePrimaria.DoesNotExist:
        alumno = EstudianteSecundaria.objects.get(id=id)
    if alumno:
        alumno.delete()
    return redirect('inicio')