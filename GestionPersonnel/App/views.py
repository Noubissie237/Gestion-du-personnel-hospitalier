from django.http import HttpResponse
import requests
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Medecin
from .serializers import MedecinSerializer
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required



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
            return render(request, 'personnel/file_d_attente.html', context={"data" : patients})
        else:
            print('Erreur lors de la récupération des patients.')

    except:
        print("erreur")
        return render(request, 'personnel/microFailed.html')
    
    # return render(request, 'personnel/file_d_attente.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'personnel/home.html', context={'name' : username})
            else:
                form.add_error(None, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/login')