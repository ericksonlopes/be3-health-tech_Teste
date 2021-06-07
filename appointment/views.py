from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from appointment.models import Appointment
from datetime import date
from register_patient.models import Paciente


@login_required
def create_appo(request, pk):
    if request.method == 'GET':
        return render(request, 'appointment/create_appo.html', {'pac': Paciente.objects.get(pk=pk)})
    try:
        if request.POST:
            Appointment.objects.create(
                pacient=Paciente.objects.get(pk=pk),
                date=request.POST['date'],
                time=request.POST['time'],
                doctorName=request.POST['doctorName']
            )
            return render(request, 'appointment/create_appo.html', {'save': 'Salvo com sucesso',
                                                                    'pac': Paciente.objects.get(pk=pk)})

    except Exception as err:

        return render(request, 'appointment/create_appo.html', {'error': err, 'pac': Paciente.objects.get(pk=pk)})


@login_required
def update_appo(request, pk):
    if request.method == 'GET':
        return render(request, 'appointment/update_appo.html',
                      {'pac': Paciente.objects.get(pk=Appointment.objects.get(pk=pk).pacient.id),
                       'appo': Appointment.objects.get(pk=pk)})

    try:
        if request.POST:
            Appointment.objects.filter(pk=pk).update(
                pacient=Paciente.objects.get(pk=Appointment.objects.get(pk=pk).pacient.id),
                date=request.POST['date'],
                time=request.POST['time'],
                doctorName=request.POST['doctorName']
            )
            return render(request, 'appointment/update_appo.html', {'save': 'Atualizado com sucesso',
                                                                    'pac': Paciente.objects.get(
                                                                        pk=Appointment.objects.get(pk=pk).pacient.id),
                                                                    'appo': Appointment.objects.get(pk=pk)})

    except Exception as err:
        return render(request, 'appointment/create_appo.html', {'error': err,
                                                                'pac': Paciente.objects.get(
                                                                    pk=Appointment.objects.get(pk=pk).pacient.id),
                                                                'appo': Appointment.objects.get(pk=pk)})


@login_required
def list_appo(request):
    return render(request, 'appointment/list_appo.html', {'appo': Appointment.objects.all(), 'datenow': date.today()})
