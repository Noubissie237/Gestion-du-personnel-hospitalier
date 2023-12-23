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


def home(request):
    return render(request, 'personnel/home.html')

def appointment(request):

    # try:
    #     url = 'http://localhost:8002/patients/'
    #     response = requests.get(url)

    #     if response.status_code == 200:
    #         patients = response.json()
    #         return render(request, 'personnel/appointment.html', context={"data" : patients})
    #     else:
    #         print('Erreur lors de la récupération des rendez-vous.')

    # except:
    #     return render(request, 'personnel/microFailed.html')

    return render(request, 'personnel/appointment.html')

def consultations(request):
    return render(request, 'personnel/consultations.html')

def prescription(request):
    return render(request, 'personnel/prescription.html')

def file_d_attente(request):

    try:
        url = 'http://localhost:8001/patients/'
        response = requests.get(url)

        if response.status_code == 200:
            patients = response.json()
            return render(request, 'personnel/file_d_attente.html', context={"data" : patients})
        else:
            print('Erreur lors de la récupération des patients.')

    except:
        print("erreur")
        return render(request, 'personnel/microFailed.html')
    
    # return render(request, 'personnel/file_d_attente.html')