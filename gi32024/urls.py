
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("entrer", views.accueil,name="url_accueil"),
    path("ok", views.home,name=""),
    path("login", views.connexion, name="url_login"),
    path("register", views.compte,name="url_register"),
    path("password", views.resetpassword,name="url_password"),
    path("logout", views.deconnexion,name="url_logout"),
    path('patient',views.afficher,name='urlaffiche'),
    path('Personnel',views.afficher_Personnel,name='urlPersonnel'),
    path('Add_Personnel',views.ajouter_Personnel,name='urladdPersonnel'),
    path('modifier-Personnel/<id>',views.modifier_Personnel,name='urlmodifierPersonnel'),
    path('supprimier-Personnel/<id>',views.supprimer_Personnel,name='urlsupprimerPersonnel'),
    path('Add_Patient',views.ajouter_Patient,name='urladdPatient'),
    path('modifier-Patient/<id>',views.modifier_Patient,name='urlmodifierPatient'),
    path('supprimier-Patient/<id>',views.supprimer_Patient,name='urlsupprimerPatient'),
    path('Examen',views.afficher_Examen,name='urlExamen'),
    path('Add_Examen',views.ajouter_Examen,name='urladdExamen'),
    path('modifier-Examen/<id>',views.modifier_Examen,name='urlmodifierExamen'),
    path('supprimier-Examen/<id>',views.supprimer_Examen,name='urlsupprimerExamen'),
    path('Salle',views.afficher_Salle,name='urlSalle'),
    path('Add_Salle',views.ajouter_Salle,name='urladdSalle'),
    path('modifier-Salle/<id>',views.modifier_Salle,name='urlmodifierSalle'),
    path('supprimier-Salle/<id>',views.supprimer_Salle,name='urlsupprimerSalle'),
    path('Service',views.afficher_Service,name='urlService'),
    path('Add_Sevices',views.ajouter_Sevices,name='urladdSevices'),
    path('modifier-Service/<id>',views.modifier_Service,name='urlmodifierService'),
    path('supprimier-Service/<id>',views.supprimer_Service,name='urlsupprimerService'),
    path('consultation',views.afficher_consultation,name='urlconsultation'),
    path('Add_consultation',views.ajouter_consultation,name='urladdconsultation'),
    path('modifier-consultation/<id>',views.modifier_consultation,name='urlmodifierconsultation'),
    path('supprimier-consultation/<id>',views.supprimer_consultation,name='urlsupprimerconsultation'),
    path('Hospitalisation',views.afficher_Hospitalisation,name='urlHospitalisation'),
    path('Add_Hospitalisation',views.ajouter_Hospitalisation,name='urladdHospitalisation'),
    path('modifier-Hospitalisation/<id>',views.modifier_Hospitalisation,name='urlmodifierHospitalisation'),
    path('supprimier-Hospitalisation/<id>',views.supprimer_Hospitalisation,name='urlsupprimerHospitalisation'),
    path("", views.base,name="url_base"),





















    
] 
