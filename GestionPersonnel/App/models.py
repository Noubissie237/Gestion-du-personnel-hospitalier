from django.db import models

# Create your models here.

class Medecin(models.Model):
    nom = models.CharField(max_length=100, null=True)
    prenom = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254, null=True)
    password = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nom

class Patient(models.Model):
    nom = models.CharField(max_length=100, null=True)
    medecin_attitré = models.ForeignKey(Medecin, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom