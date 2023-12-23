from django.contrib import admin
from .models import *

# Register your models here.
class medecinAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'password')

class patientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'medecin_attitré')

admin.site.register(Medecin, medecinAdmin)
admin.site.register(Patient, patientAdmin)