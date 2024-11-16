from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.inicio, name='inicio'),
    path('primaria/', v.inicio_primaria, name='inicio_primaria'),
    path('secundaria/', v.inicio_secundaria, name='inicio_secundaria'),
    path('new', v.alumno_new, name='alumno_new'),
    path('edit/<int:id>/', v.alumno_update, name='alumno_update'),
    path('delete/<int:id>/', v.alumno_delete, name='alumno_delete'),
]