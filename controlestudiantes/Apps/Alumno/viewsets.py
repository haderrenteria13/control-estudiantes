from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlumnoViewSetPrimaria, AlumnoViewSetSecundaria

router = DefaultRouter()
router.register(r'estudiantes-primaria', AlumnoViewSetPrimaria)
router.register(r'estudiantes-secundaria', AlumnoViewSetSecundaria)

urlpatterns = [
    path('', include(router.urls)),
]