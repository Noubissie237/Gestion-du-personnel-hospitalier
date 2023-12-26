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
    nom = forms.CharField(label='Nom', widget=forms.TextInput(attrs={'class': 'input--style-1'}))
    prenom = forms.CharField(label='Prénom', widget=forms.TextInput(attrs={'class': 'input--style-1'}))
    age = forms.IntegerField(required=False, label="Age", widget=forms.TextInput(attrs={'class': 'input--style-1'}))
    sexe = forms.CharField(required=False, label="Sexe",  widget=forms.TextInput(attrs={'class': 'input--style-1'}))
    email = forms.EmailField(required=True, label="Email",  widget=forms.TextInput(attrs={'class': 'input--style-1'}))
    prescription1 = forms.CharField(required=False, label="Prescription", widget=forms.TextInput(attrs={'class': 'input--style-1'}))
    prescription2 = forms.CharField(required=False, label="Prescription", widget=forms.TextInput(attrs={'class': 'input--style-1'}))
    prescription3 = forms.CharField(required=False, label="Prescription", widget=forms.TextInput(attrs={'class': 'input--style-1'}))
