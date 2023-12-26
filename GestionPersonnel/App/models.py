from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Specialite(models.Model):
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.designation

class Medecin(AbstractUser):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null=False, unique=True)
    Specialite = models.ForeignKey(Specialite, null=True, on_delete=models.SET_NULL)
    password = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.nom

# class Consultation(models.Model):
#     pass

class Prescription(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    sexe = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, null=False)
    antecedent = models.TextField(null=True)
    prescription1 = models.CharField(max_length=150, null=True)
    prescription2 = models.CharField(max_length=150, null=True)
    prescription3 = models.CharField(max_length=150, null=True)
    Date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom