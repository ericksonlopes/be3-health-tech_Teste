from django.shortcuts import render
from appointment.models import Appointment


# Create your views here.
def list_appo(request):
    return render(request, 'appointment/list_appo.html', {'appo': Appointment.objects.all()})
