from django import forms
from django.forms.widgets import PasswordInput

class PasswordInputWithClass(PasswordInput):
    def __init__(self, attrs=None):
        if attrs is None:
            
            attrs = {}
        attrs['class'] = 'form-control'
        super().__init__(attrs)


class LoginForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisateur', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Mot de passe', widget=PasswordInputWithClass())


class PrescriptionForm(forms.Form):
    nom = forms.CharField(label='Nom', widget=forms.TextInput(attrs={'class': 'form-control'}))
    prenom = forms.CharField(label='Prénom', widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(required=False, label="Age")
    sexe = forms.CharField(required=False, label="Sexe")
    email = forms.EmailField(required=True, label="Email")
    prescription1 = forms.CharField(required=False, label="Prescription",)
    prescription2 = forms.CharField(required=False, label="Prescription",)
    prescription3 = forms.CharField(required=False, label="Prescription",)