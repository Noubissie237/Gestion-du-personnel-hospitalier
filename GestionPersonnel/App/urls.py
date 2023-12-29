from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'prescriptions', PrescriptionViewSet)

urlpatterns = [
    path('api', include(router.urls)),
    path('', home),
    path('home/', home),
    path('rendez-vous/', appointment),
    path('consultations/', consultations),
    path('prescription/', prescription),
    path('file-d-attente/', file_d_attente),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('patient/', patient),
]
