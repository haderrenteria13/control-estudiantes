from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstudiantePrimariaViewSet, EstudianteSecundariaViewSet
from . import views as v

router = DefaultRouter()
router.register(r'estudiantes-primaria', EstudiantePrimariaViewSet)
router.register(r'estudiantes-secundaria', EstudianteSecundariaViewSet)

urlpatterns = [
    path('primaria/', v.inicio_primaria, name='inicio_primaria'),
    path('secundaria/', v.inicio_secundaria, name='inicio_secundaria'),
    path('new/', v.alumno_new, name='alumno_new'),
    path('edit/<str:etapa>/<int:id>/', v.alumno_update, name='alumno_update'),
    path('delete/<int:id>/', v.alumno_delete, name='alumno_delete'),
    path('api/', include(router.urls)),  # Asegúrate de que esta línea esté presente
    path('', v.inicio, name='inicio'),
]