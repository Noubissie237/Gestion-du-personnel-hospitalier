from django.http import HttpResponse
import requests
from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient, Medecin
from .serializers import PatientSerializer, MedecinSerializer

class MedecinViewSet(viewsets.ModelViewSet):
    queryset = Medecin.objects.all()
    serializer_class = MedecinSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

def listDePatients(request):
    try:
        url = 'http://localhost:8001/patients/'
        response = requests.get(url)

        if response.status_code == 200:
            patients = response.json()
            return render(request, 'listDePatient.html', context={"data" : patients})
        else:
            print('Erreur lors de la récupération des patients.')

    except:
        return HttpResponse("<h1 align='center' style='color:red'>Le micro service en charge de la gestion des patients semble être indisponible</h1>")

