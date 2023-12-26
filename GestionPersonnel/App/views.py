from django.http import HttpResponse
import requests
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Medecin, Prescription
from .serializers import MedecinSerializer
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, PrescriptionForm
from django.contrib.auth.decorators import login_required
import json


class MedecinViewSet(viewsets.ModelViewSet):
    queryset = Medecin.objects.all()
    serializer_class = MedecinSerializer

@login_required(login_url='/login')
def home(request):
    return render(request, 'personnel/home.html')

@login_required(login_url='/login')
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

@login_required(login_url='/login')
def consultations(request):
    return render(request, 'personnel/consultations.html')

@login_required(login_url='/login')
def prescription(request):
    return render(request, 'personnel/prescription.html')

@login_required(login_url='/login')
def file_d_attente(request):

    try:
        url = 'http://localhost:8001/patients/'
        response = requests.get(url)

        if response.status_code == 200:
            patients = response.json()
            for elt in patients:         
                if elt['service'] == 1:
                    elt['service']  = 'RADIOLOGUE'
                elif elt['service'] == 2:
                    elt['service']  = 'PSYCHIATRE'
                elif elt['service'] == 3:
                    elt['service']  = 'PEDIATRE'
                elif elt['service'] == 4:
                    elt['service']  = 'OPHTAMOLOGUE'
                elif elt['service'] == 5:
                    elt['service']  = 'NEUROLOGUE'
                elif elt['service'] == 6:
                    elt['service']  = 'GYNECOLOGUE'
                elif elt['service'] == 7:
                    elt['service']  = 'GENERALISTE'
                elif elt['service'] == 8:
                    elt['service']  = 'DENTISTE'
                elif elt['service'] == 9:
                    elt['service']  = 'CHIRURGIEN'
                elif elt['service'] == 10:
                    elt['service']  = 'CARDIOLOGUE'
            
            return render(request, 'personnel/file_d_attente.html', context={"data" : patients})
        else:
            print('Erreur lors de la récupération des patients.')

    except:
        print("erreur")
        return render(request, 'personnel/microFailed.html')
    
    # return render(request, 'personnel/file_d_attente.html')

@login_required(login_url='/login')
def patient(request, link_Id):
    if request.method == 'POST':
        data = request.POST
        
        dataToSave = PrescriptionForm(request.POST)
        if dataToSave.is_valid():
            print("Successs")
            pushit = Prescription.objects.create(nom=data['nom'], prenom=data['prenom'], 
                                                age=data['age'], sexe=data['sexe'], email=data['email'],
                                                antecedent=data['antecedent'], prescription1=data['presc1'],
                                                prescription2=data['presc2'], prescription3=data['presc3']
                                                )

        else:
            print("Failed")

    else:
        pass

    return render(request, 'personnel/patient.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'personnel/home.html', context={'name' : request.user.username})
            else:
                form.add_error(None, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/login')