from django.shortcuts import render
from register_patient.models import Paciente
from django.contrib.auth.decorators import login_required
from appointment.models import Appointment
from health_insurance.models import HealthInsurance
from doctor.models import Doctor


@login_required
def homepage(request):
    list_conv = [item.name for item in HealthInsurance.objects.all()]

    if len(Paciente.objects.all()) == 0:
        porc_conv = [{'qtd': 0,
                      'conv': conv,
                      'porc': 0
                      } for conv in list_conv]
    else:
        porc_conv = [{'qtd': len(Paciente.objects.filter(convenio=conv)),
                      'conv': conv,
                      'porc': f'{(len(Paciente.objects.filter(convenio=conv)) / len(Paciente.objects.all())) * 100:.4}'
                      } for conv in list_conv]

    return render(request, 'home.html', {'len_pac': len(Paciente.objects.all()),
                                         'porc_conv': porc_conv,
                                         'len_appo': len(Appointment.objects.all()),
                                         'len_conv': len(HealthInsurance.objects.all()),
                                         'len_dc': len(Doctor.objects.all())})
