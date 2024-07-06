from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#importation du modele user
from django.contrib.auth.models import User
#importation des modules d'authentification
from django.contrib.auth import login, authenticate, logout

from app1.models import Personnel, Consultation,Salle,Service, Hospitalisation,Examen, Patient_examin
# Create your views here.

#Authentification

#connexion
def connexion(request):
    if request.method == 'POST':
        data=request.POST
        username=data.get('username')
        password=data.get('password')
        print(f"E-mail: {username}, Passwor: {password}")
        #if username is not None and password is not None:
        user= authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect("url_accueil")
        else:
            print("Wrong data The login went wrong sorry")
            return redirect("url_login")
        #else:
            #print("empty data sorry try again")
            #return redirect("url_login")

    return render(request, "auth/login.html")

#creation compte
def compte(request):
    if request.method == 'POST':
        data=request.POST
        a= data.get('username')
        b= data.get('email')
        c= data.get('password')
        print(f" Name: {a}\nE-mail: {b}\nPassword: {c}\n")
        #if username is not None and email is not None and password is not None:
        toto= User.objects.create_user(username=data.get('username'), email=data.get('email'), password=data.get('password'))
    print("Null values the user wasn't created sorry try again")
    return render(request, 'auth/register.html')

#modification mot de passe via mail
def resetpassword(request):

    return render(request, 'auth/password.html')

#deconnexion
def deconnexion(request):
    logout(request)
    return redirect("url_login")


#Site
@login_required(login_url='url_login')



def home(request):

    return render(request, 'site/base.html')

@login_required(login_url='url_login')
def accueil(request):

    return render(request, 'site/home.html')

@login_required(login_url='url_login')
def afficher(request):
    data=Patient_examin.objects.all()
    toto={'tata':data}
    return render(request,'Patient_examin/affiche.html',toto) 

@login_required(login_url='url_login')
def ajouter_Patient(request):
    if request.method=="POST":
        valeur=request.POST
        examen=valeur.get('examen')
        nom=valeur.get('nom')
        prenom=valeur.get('prenom')
        telephone=valeur.get('telephone')
        sexe=valeur.get('sexe')
        age=valeur.get('age')
        medecin=valeur.get('medecin')
        date=valeur.get('date')
        data=Patient_examin.objects.create(nom=nom,prenom=prenom,telephone=telephone,sexe=sexe,age=age,medecin=medecin,date=date)
        ok=Patient_examin.objects.all()
        print(ok)
        return redirect('urlaffiche')

    return render(request,'Patient_examin/ajouter.html')

@login_required(login_url='url_login')
def modifier_Patient(request,id):
    data=Patient_examin.objects.get(id=id)
    if request.method=="POST":
        valeur=request.POST
        data.examen=valeur.get('examen')
        data.nom=valeur.get('nom')
        data.prenom=valeur.get('prenom')
        data.telephone=valeur.get('telephone')
        data.sexe=valeur.get('sexe')
        data.age=valeur.get('age')
        data.medecin=valeur.get('medecin')
        data.date=valeur.get('date')
        data.save()
        return redirect('urlPersonnel')
    return render(request,'Patient_examin/modifier.html',{'data':data}) 

def supprimer_Patient(request,id):
    data=Patient_examin.objects.get(id=id)
    data.delete()
    return redirect('urlaffiche') 


@login_required(login_url='url_login')
def afficher_Personnel(request):
    data=Personnel.objects.all()
    toto={'tata':data}
    return render(request,'Personnel/affiche.html',toto) 

@login_required(login_url='url_login')
def ajouter_Personnel(request):
    if request.method=="POST":
        valeur=request.POST
        nom=valeur.get('nom')
        prenom=valeur.get('prenom')
        telephone=valeur.get('telephone')
        email=valeur.get('email')
        adresse=valeur.get('adresse')
        statut=valeur.get('statut')
        date=valeur.get('date')
        data=Personnel.objects.create(nom=nom,prenom=prenom,telephone=telephone,email=email,adresse=adresse,statut=statut,date=date)
        ok=Personnel.objects.all()
        print(ok)
        return redirect('urlPersonnel')

    return render(request,'Personnel/ajouter.html')

@login_required(login_url='url_login')
def modifier_Personnel(request,id):
    data=Personnel.objects.get(id=id)
    if request.method=="POST":
        valeur=request.POST
        data.nom=valeur.get('nom')
        data.prenom=valeur.get('prenom')
        data.telephone=valeur.get('telephone')
        data.email=valeur.get('email')
        data.adresse=valeur.get('adresse')
        data.statut=valeur.get('statut')
        data.date=valeur.get('date')
        data.save()
        return redirect('urlPersonnel')
    return render(request,'Personnel/modifier.html',{'data':data}) 

def supprimer_Personnel(request,id):
    data=Personnel.objects.get(id=id)
    data.delete()
    return redirect('urlPersonnel') 

    
@login_required(login_url='url_login')
def afficher_Examen(request):
    data=Examen.objects.all()
    toto={'tata':data}
    return render(request,'Examen/affiche.html',toto) 


@login_required(login_url='url_login')
def ajouter_Examen(request):
    if request.method=="POST":
        valeur=request.POST
        nom=valeur.get('nom')
        type=valeur.get('type')
        data=Examen.objects.create(nom=nom,type=type)
        ok=Examen.objects.all()
        print(ok)
        return redirect('urlExamen')

    return render(request,'Examen/ajouter.html')

def modifier_Examen(request,id):
    data=Examen.objects.get(id=id)
    if request.method=="POST":
        valeur=request.POST
        data.nom=valeur.get('nom')
        data.type=valeur.get('type')
        data.save()
        return redirect('urlExamen')
    return render(request,'Examen/modifier.html',{'data':data}) 

def supprimer_Examen(request,id):
    data=Examen.objects.get(id=id)
    data.delete()
    return redirect('urlExamen') 


@login_required(login_url='url_login')
def afficher_Salle(request):
    data=Salle.objects.all()
    toto={'tata':data}
    return render(request,'Salle/affiche.html',toto) 

@login_required(login_url='url_login')
def ajouter_Salle(request):
    if request.method=="POST":
        valeur=request.POST
        nom=valeur.get('nom')
        numero=valeur.get('numero')
        nbrepatient=valeur.get('nbrepatient')
        date=valeur.get('date')
        data=Salle.objects.create(nom=nom,numero=numero,nbrepatient=nbrepatient,date=date)
        ok=Salle.objects.all()
        print(ok)
        return redirect('urlSalle')

    return render(request,'Salle/ajouter.html')

@login_required(login_url='url_login')
def modifier_Salle(request,id):
    data=Salle.objects.get(id=id)
    if request.method=="POST":
        valeur=request.POST
        data.nom=valeur.get('nom')
        data.numero=valeur.get('numero')
        data.nbrepatient=valeur.get('nbrepatient')
        data.date=valeur.get('date')
        data.save()
        return redirect('urlSalle')
    return render(request,'Salle/modifier.html',{'data':data}) 

def supprimer_Salle(request,id):
    data=Salle.objects.get(id=id)
    data.delete()
    return redirect('urlSalle')
    
@login_required(login_url='url_login')
def afficher_Service(request):
    data=Service.objects.all()
    toto={'tata':data}
    return render(request,'Service/affiche.html',toto) 

@login_required(login_url='url_login')
def ajouter_Sevices(request):
    if request.method=="POST":
        valeur=request.POST
        nom=valeur.get('nom')
        responsable=valeur.get('responsable')
        adjoint=valeur.get('adjoint')
        data=Service.objects.create(nom=nom,responsable=responsable,adjoint=adjoint)
        ok=Service.objects.all()
        print(ok)
        return redirect('urlService')

    return render(request,'Service/ajouter.html')

@login_required(login_url='url_login')
def modifier_Service(request,id):
    data=Service.objects.get(id=id)
    if request.method=="POST":
        valeur=request.POST
        data.nom=valeur.get('nom')
        data.responsable=valeur.get('responsable')
        data.adjoint=valeur.get('adjoint')
        data.save()
        return redirect('urlService')
    return render(request,'Service/modifier.html',{'data':data}) 

def supprimer_Service(request,id):
    data=Service.objects.get(id=id)
    data.delete()
    return redirect('urlService')

@login_required(login_url='url_login')
def afficher_consultation(request):
    data=Consultation.objects.all()
    toto={'tata':data}
    return render(request,'Consultation/affiche.html',toto) 

@login_required(login_url='url_login')
def ajouter_consultation(request):
    if request.method=="POST":
        valeur=request.POST
        nom=valeur.get('nom')
        prenom=valeur.get('prenom')
        sexe=valeur.get('sexe')
        age=valeur.get('age')
        poids=valeur.get('poids')
        telephone=valeur.get('telephone')
        adresse=valeur.get('adresse')
        observation=valeur.get('observation')
        date=valeur.get('date')
        data=Consultation.objects.create(nom=nom,prenom=prenom,sexe=sexe,age=age,poids=poids,telephone=telephone,adresse=adresse,observation=observation,date=date)
        ok=Consultation.objects.all()
        print(ok)
        return redirect('urlconsultation')

    return render(request,'Consultation/ajouter.html')

@login_required(login_url='url_login')
def modifier_consultation(request,id):
    data=Consultation.objects.get(id=id)
    if request.method=="POST":
        valeur=request.POST
        data.nom=valeur.get('nom')
        data.prenom=valeur.get('prenom')
        data.sexe=valeur.get('sexe')
        data.age=valeur.get('age')
        data.poids=valeur.get('poids')
        data.telephone=valeur.get('telephone')
        data.adresse=valeur.get('adresse')
        data.observation=valeur.get('observation')
        data.date=valeur.get('date')
        data.save()
        return redirect('urlconsultation')
    return render(request,'Consultation/modifier.html',{'data':data}) 

def supprimer_consultation(request,id):
    data=Consultation.objects.get(id=id)
    data.delete()
    return redirect('urlconsultation')

@login_required(login_url='url_login')
def afficher_Hospitalisation(request):
    data=Hospitalisation.objects.all()
    toto={'tata':data}
    return render(request,'Hospitalisation/affiche.html',toto) 


@login_required(login_url='url_login')
def ajouter_Hospitalisation(request):
    if request.method=="POST":
        valeur=request.POST
        nom=valeur.get('nom')
        prenom=valeur.get('prenom')
        sexe=valeur.get('sexe')
        age=valeur.get('age')
        poids=valeur.get('poids')
        telephone=valeur.get('telephone')
        adresse=valeur.get('adresse')
        observation=valeur.get('observation')
        date_hosp=valeur.get('date_hosp')
        date_sorti=valeur.get('date_sorti')
        data=Hospitalisation.objects.create(nom=nom,prenom=prenom,sexe=sexe,age=age,poids=poids,telephone=telephone,adresse=adresse,observation=observation,date_hosp=date_hosp,date_sorti=date_sorti)
        ok=Hospitalisation.objects.all()
        print(ok)
        return redirect('urlHospitalisation')

    return render(request,'Hospitalisation/ajouter.html')  

@login_required(login_url='url_login')
def modifier_Hospitalisation(request,id):
    data=Hospitalisation.objects.get(id=id)
    if request.method=="POST":
        valeur=request.POST
        data.nom=valeur.get('nom')
        data.prenom=valeur.get('prenom')
        data.sexe=valeur.get('sexe')
        data.age=valeur.get('age')
        data.poids=valeur.get('poids')
        data.telephone=valeur.get('telephone')
        data.adresse=valeur.get('adresse')
        data.observation=valeur.get('observation')
        data.date_hosp=valeur.get('date_hosp')
        data.date_sorti=valeur.get('date_sorti')
        data.save()
        return redirect('urlHospitalisation')
    return render(request,'Hospitalisation/modifier.html',{'data':data}) 

def supprimer_Hospitalisation(request,id):
    data=Hospitalisation.objects.get(id=id)
    data.delete()
    return redirect('urlHospitalisation')


@login_required(login_url='url_login')
def base(request):

    return render(request, 'site/accueil.html')














    