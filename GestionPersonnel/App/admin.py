from django.contrib import admin
from .models import *

# Register your models here.
class medecinAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'password')

class specialiteAdmin(admin.ModelAdmin):
    list_display = ('designation',)

admin.site.register(Medecin, medecinAdmin)
admin.site.register(Specialite, specialiteAdmin)
