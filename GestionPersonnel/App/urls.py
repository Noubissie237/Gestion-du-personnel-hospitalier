from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'medecins', MedecinViewSet)
router.register(r'patients', PatientViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', home),
    path('home/', home),
    path('rendez-vous/', appointment),
    path('consultations/', consultations),
    path('prescription/', prescription),
    path('file-d-attente/', file_d_attente),
]
