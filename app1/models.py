from django.db import models

# Create your models here.


class Examen(models.Model):
    type=models.CharField(max_length=100)
    nom=models.CharField(max_length=100)

    def __str__(self):

        return f"Type {self.type}/ Nom {self.nom}"
    
class Salle(models.Model):
    nom=models.CharField(max_length=100)
    numero=models.IntegerField()
    nbrepation=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"Nom {self.nom} Numéro {self.numero} "

class Personnel(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    telephone=models.CharField(max_length=100)
    email=models.EmailField()
    adresse=models.CharField(max_length=100)
    statut=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)

    def __str__(self):

        return self.nom
    


class Service(models.Model):
    nom=models.CharField(max_length=100)
    responsable=models.CharField(max_length=100, unique=True)
    adjoint=models.CharField(max_length=100, unique=True)
    
    def __str__(self):

        return f"Nom {self.nom}" 
    
class Patient_examin(models.Model):
    examen=models.CharField(max_length=100)
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    telephone=models.CharField(max_length=100)
    sexe=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    medecin=models.ForeignKey(Personnel, on_delete=models.CASCADE, related_name='personnel')
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"Nom {self.nom}"
    
class Consultation(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    sexe=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    poids=models.CharField(max_length=100)
    telephone=models.CharField(max_length=100)
    adresse=models.CharField(max_length=100)
    observetion=models.CharField(max_length=900)
    date=models.DateField(auto_now=True)
    
    def __str__(self):

        return f"Nom {self.nom}"
    
class Hospitalisation(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    sexe=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    poids=models.CharField(max_length=100)
    observation=models.CharField(max_length=100)
    examen=models.CharField(max_length=100)
    telephone=models.CharField(max_length=100)
    adresse=models.CharField(max_length=100)
    date_hosp=models.DateField(auto_now=True)
    date_sorti=models.DateField(null=True)

    def __str__(self):

        return f"Nom {self.nom}"