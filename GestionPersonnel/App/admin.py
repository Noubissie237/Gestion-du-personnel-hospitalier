from django.contrib import admin
from .models import *

# Register your models here.
class medecinAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'password')

class specialiteAdmin(admin.ModelAdmin):
    list_display = ('designation',)

class prescriptionAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'age', 'sexe', 'email', 'antecedent','prescription1', 'prescription2', 'prescription3', 'Date')


admin.site.register(Medecin, medecinAdmin)
admin.site.register(Specialite, specialiteAdmin)
admin.site.register(Prescription, prescriptionAdmin)