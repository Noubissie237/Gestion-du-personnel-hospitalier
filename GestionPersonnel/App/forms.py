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
