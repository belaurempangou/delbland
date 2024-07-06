from django.contrib import admin
from app1.models import Personnel,Patient_examin,Hospitalisation,Consultation,Service,Salle
# Register your models here.

admin.site.register(Personnel)
admin.site.register(Patient_examin)
admin.site.register(Hospitalisation)
admin.site.register(Consultation)
admin.site.register(Service)
admin.site.register(Salle)
