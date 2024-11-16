from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Alummno
from .form import AlumnoForm

@login_required
def inicio(request):
    query = request.GET.get('q')
    if query:
        alumnos = Alummno.objects.filter(nombre__icontains=query) | Alummno.objects.filter(apellido__icontains=query) | Alummno.objects.filter(edad__icontains=query) | Alummno.objects.filter(sexo__icontains=query) | Alummno.objects.filter(telefono__icontains=query)
    else:
        alumnos = Alummno.objects.all()
    context = {
        'valumno': alumnos,
        'query': query,
    }
    return render(request, 'Alumno/inicio.html', context)

@login_required
def alumno_new(request):
    if request.method == 'POST':
        alumno_form = AlumnoForm(request.POST)
        if alumno_form.is_valid():
            alumno_form.save()
            return redirect('inicio')
    else:
        alumno_form = AlumnoForm()
    return render(request, 'Alumno/alumno_form.html', {'alumno_form': alumno_form})

@login_required
def alumno_update(request, id):
    alummno = get_object_or_404(Alummno, id=id)
    if request.method == 'POST':
        alumno_form = AlumnoForm(request.POST, instance=alummno)
        if alumno_form.is_valid():
            alumno_form.save()
            return redirect('inicio')
    else:
        alumno_form = AlumnoForm(instance=alummno)
    return render(request, 'Alumno/alumno_form.html', {'alumno_form': alumno_form})

@login_required
def alumno_delete(request, id):
    alummno = get_object_or_404(Alummno, id=id)
    if alummno:
        alummno.delete()
    return redirect('inicio')
