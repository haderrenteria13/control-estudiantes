from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import EstudiantePrimaria, EstudianteSecundaria
from .form import AlumnoForm
from django.db.models import Q
from django.core.paginator import Paginator
from itertools import chain
from rest_framework import viewsets
from .serializer import EstudiantePrimariaSerializer, EstudianteSecundariaSerializer



@login_required
def inicio(request):
    query = request.GET.get('q')
    if query:
        estudiantes_primaria = EstudiantePrimaria.objects.filter(
            Q(_nombre__icontains=query) | 
            Q(_apellido__icontains=query)
        )
        estudiantes_secundaria = EstudianteSecundaria.objects.filter(
            Q(_nombre__icontains=query) | 
            Q(_apellido__icontains=query)
        )
    else:
        estudiantes_primaria = EstudiantePrimaria.objects.all()
        estudiantes_secundaria = EstudianteSecundaria.objects.all()

    # Combinar las listas de estudiantes
    estudiantes = list(chain(estudiantes_primaria, estudiantes_secundaria))

    # Paginación
    paginator = Paginator(estudiantes, 10)  # 10 estudiantes por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'estudiantes_primaria': estudiantes_primaria,
        'estudiantes_secundaria': estudiantes_secundaria,
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
    
    estudiantes_secundaria = EstudianteSecundaria.objects.all()  # Asegúrate de obtener también los estudiantes de secundaria

    context = {
        'estudiantes_primaria': estudiantes_primaria,
        'estudiantes_secundaria': estudiantes_secundaria,  # Pasar al contexto
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
    
    estudiantes_primaria = EstudiantePrimaria.objects.all()  # Asegúrate de obtener también los estudiantes de primaria

    context = {
        'estudiantes_secundaria': estudiantes_secundaria,
        'estudiantes_primaria': estudiantes_primaria,  # Pasar al contexto
        'query': query,
    }
    return render(request, 'Alumno/secundaria.html', context)

@login_required
def alumno_new(request):
    if request.method == 'POST':
        alumno_form = AlumnoForm(request.POST)
        if alumno_form.is_valid():
            tipo_alumno = alumno_form.cleaned_data.pop('tipo_alumno')
            media = alumno_form.cleaned_data.pop('media', False)
            cleaned_data = {key: value for key, value in alumno_form.cleaned_data.items()}
            if tipo_alumno == 'primaria':
                alumno = EstudiantePrimaria.crear_estudiante(**cleaned_data)
            else:
                alumno = EstudianteSecundaria.crear_estudiante(**cleaned_data, media=media)
            alumno.save()
            return redirect('inicio')
    else:
        alumno_form = AlumnoForm()
    return render(request, 'Alumno/alumno_form.html', {'alumno_form': alumno_form})

@login_required
def alumno_update(request, id):
    next_url = request.GET.get('next', 'inicio')
    try:
        alumno = EstudiantePrimaria.objects.get(id=id)
        tipo_alumno = 'primaria'
    except EstudiantePrimaria.DoesNotExist:
        alumno = EstudianteSecundaria.objects.get(id=id)
        tipo_alumno = 'secundaria'

    if request.method == 'POST':
        alumno_form = AlumnoForm(request.POST, instance=alumno)
        if alumno_form.is_valid():
            tipo_alumno_nuevo = alumno_form.cleaned_data.pop('tipo_alumno')
            media = alumno_form.cleaned_data.pop('media', False)
            cleaned_data = {key: value for key, value in alumno_form.cleaned_data.items()}
            grado_nuevo = cleaned_data.get('_grado')

            # Determinar el nuevo tipo de alumno basado en el grado
            if grado_nuevo in ["1", "2", "3", "4", "5"]:
                tipo_alumno_nuevo = 'primaria'
            elif grado_nuevo in ["6", "7", "8", "9", "10", "11"]:
                tipo_alumno_nuevo = 'secundaria'

            if tipo_alumno != tipo_alumno_nuevo:
                # Cambiar el tipo de alumno
                if tipo_alumno_nuevo == 'primaria':
                    alumno_nuevo = EstudiantePrimaria.crear_estudiante(**cleaned_data)
                else:
                    alumno_nuevo = EstudianteSecundaria.crear_estudiante(**cleaned_data, media=media)
                alumno.delete()
                alumno_nuevo.save()
            else:
                if tipo_alumno == 'secundaria':
                    alumno.media = media
                alumno_form.save()
            return redirect(next_url)
    else:
        alumno_form = AlumnoForm(instance=alumno)
        alumno_form.fields['tipo_alumno'].initial = tipo_alumno
    return render(request, 'Alumno/alumno_form.html', {'alumno_form': alumno_form, 'next': next_url})

@login_required
def alumno_delete(request, id):
    try:
        alumno = EstudiantePrimaria.objects.get(id=id)
    except EstudiantePrimaria.DoesNotExist:
        alumno = EstudianteSecundaria.objects.get(id=id)
    if alumno:
        alumno.delete()
    return redirect('inicio')

class EstudiantePrimariaViewSet(viewsets.ModelViewSet):
    queryset = EstudiantePrimaria.objects.all()
    serializer_class = EstudiantePrimariaSerializer

class EstudianteSecundariaViewSet(viewsets.ModelViewSet):
    queryset = EstudianteSecundaria.objects.all()
    serializer_class = EstudianteSecundariaSerializer