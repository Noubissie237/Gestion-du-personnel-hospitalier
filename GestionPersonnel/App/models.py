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

class Consultation(models.Model):
    pass

class Prescription(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=254, unique=True)
    sexe = models.CharField(max_length=15)
    age = models.IntegerField(null=True)
    poids = models.IntegerField(null=True)
    antecedent = models.TextField(null=True)
    prescription = models.TextField(null=True)
