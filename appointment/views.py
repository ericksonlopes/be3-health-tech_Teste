from django.shortcuts import render
from appointment.models import Appointment
from datetime import date


# Create your views here.
def list_appo(request):
    return render(request, 'appointment/list_appo.html', {'appo': Appointment.objects.all(), 'datenow': date.today()})
