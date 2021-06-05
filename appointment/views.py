from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from appointment.models import Appointment
from datetime import date


@login_required
def create_appo(request):
    if request.method == 'GET':
        return render(request, 'appointment/create_appo.html')


@login_required
def update_appo(request, pk):
    if request.method == 'GET':
        return render(request, 'appointment/update_appo.html', {'appo': Appointment.objects.get(pk=pk)})


@login_required
def list_appo(request):
    return render(request, 'appointment/list_appo.html', {'appo': Appointment.objects.all(), 'datenow': date.today()})
