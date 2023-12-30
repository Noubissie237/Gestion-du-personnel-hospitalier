from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Medecin, Prescription, Consultation
from .serializers import PrescriptionSerializer
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, PrescriptionForm
from django.contrib.auth.decorators import login_required
import json, base64, requests, datetime, hashlib, random, string
from GestionPersonnel import settings
from django.contrib import messages
from django.core.mail import send_mail


from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

def generer_mot_de_passe():
    caracteres = string.ascii_letters + string.digits
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(8))
    return mot_de_passe

@login_required(login_url='/login')
def home(request):

    # # Récupérer les données de la requête POST
    # username = request.POST.get('username')
    # password = request.POST.get('password')

    # # Si les identifiants sont valides, faites une requête à l'API d'authentification pour obtenir un token
    # response = requests.post('http://localhost:2370/login/', data={'username': username, 'password': password})

    # if response.status_code == 200:
    #     token = response.json().get('token')
    #     print(token)
    # else:
    #     print('Erreur')

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
    
    if request.method == 'POST':

        data = request.POST

        data = Prescription.objects.filter(email=data['pk']).values()

        data = json.dumps(list(data))

        data = json.loads(data)

        data = data[0]

        print(data)
            
        json_data = json.dumps(data)

        encoded_data = base64.urlsafe_b64encode(json_data.encode()).decode()

        return HttpResponseRedirect(('/prescription') + f'?data={encoded_data}')

    else:

        patient = Consultation.objects.filter(status=True).values()
                
        patient = json.dumps(list(patient))

        patient = json.loads(patient)

        patient = modif(patient)

        return render(request, 'personnel/consultations.html', context={"data" : patient})
    
@login_required(login_url='/login')
def prescription(request):

    try:
        encoded_data = request.GET.get('data')

        decoded_data = base64.urlsafe_b64decode(encoded_data).decode()

        data = json.loads(decoded_data)

        person = {}

        tmp = {}

        for key, value in data.items():
            tmp[key] = value
            person = (tmp)

        return render(request, 'personnel/prescription.html', context={"data" : person})
    except:
        return render(request, 'personnel/notPatient.html')

def modif(dataset):
    for elt in dataset:         
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

    return dataset

@login_required(login_url='/login')
def file_d_attente(request):

    try:
        url = 'http://localhost:8001/patients/'
        response = requests.get(url)
        dataToSave = response.json()

        for elt in dataToSave:
            if Consultation.objects.filter(email=elt['email']).exists():
                pass
            else:
                tmp = Consultation(nom=elt['nom'],prenom=elt['prenom'], email=elt['email'], age=elt['age'], service=elt['service'], sexe=elt['sexe'])
                tmp.save()

        if response.status_code == 200:

            if request.method == 'POST':

                data = request.POST

                patients = response.json()

                data = Consultation.objects.filter(email=data['pk']).values()

                data = json.dumps(list(data))

                data = json.loads(data)

                data = modif(data)

                data = data[0]
            
                json_data = json.dumps(data)

                encoded_data = base64.urlsafe_b64encode(json_data.encode()).decode()

                return HttpResponseRedirect(('/patient') + f'?data={encoded_data}')
            
            else:

                patient = Consultation.objects.filter(status=False).values()
                
                patient = json.dumps(list(patient))

                patient = json.loads(patient)

                patient = modif(patient)

                return render(request, 'personnel/file_d_attente.html', context={"data" : patient})
        else:

            print('Erreur lors de la récupération des patients.')

    except:

        return render(request, 'personnel/microFailed.html')

@login_required(login_url='/login')
def patient(request):

    encoded_data = request.GET.get('data')
    
    decoded_data = base64.urlsafe_b64decode(encoded_data).decode()

    data = json.loads(decoded_data)

    person = {}

    tmp = {}

    for key, value in data.items():
        tmp[key] = value
        person = (tmp)

    if request.method == 'POST':

        data = request.POST

        req = Consultation.objects.get(email=data['email'])
                
        req.status = True
 
        req.save()

        mdp = generer_mot_de_passe()

        dataToSave = PrescriptionForm(request.POST)

        if dataToSave.is_valid():

            pushit = Prescription(nom=data['nom'], prenom=data['prenom'], 
                                                age=data['age'], sexe=data['sexe'], email=data['email'],
                                                antecedent=data['antecedent'], prescription1=data['presc1'],
                                                prescription2=data['presc2'], prescription3=data['presc3'], Token=mdp
                                                )
            
            pushit.save()

            mail = data['email']

            subject = "ACCES A LA PHARMACIE"

            message = "Hey M./Mme {}, accedez a notre pharmacie et achetez vos medicaments en toute securité!! \nRendez-vous vers le site approprié et entrer comme information de connexion les informations ci-dessous : \n\nUSERNAME : {}\nPASSWORD : {}\n".format(data['nom'], mail, mdp)
            
            from_email = settings.EMAIL_HOST_USER

            to_list = [mail]

            send_mail(subject, message, from_email, to_list, fail_silently=True)

            
            return HttpResponseRedirect('/file-d-attente')
        
        else:

            pass

    else:

        return render(request, 'personnel/patient.html', context={"data" : person})

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

