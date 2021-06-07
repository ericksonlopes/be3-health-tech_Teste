from django.contrib import admin
from appointment.models import Appointment


@admin.register(Appointment)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['pacient', 'date', 'time', 'doctorName']
