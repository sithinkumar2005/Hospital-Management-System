from django.contrib import admin
from.models import patient,doctor,Appointment


# Register your models here.
admin.site.register(patient)
admin.site.register(doctor)
admin.site.register(Appointment)