from django.shortcuts import render
from register_patient.models import Paciente
from django.contrib.auth.decorators import login_required


@login_required
def homepage(request):
    list_conv = ['SulAmérica', 'NotreDame Intermédica', 'Prevent Senior', 'Assim Saúde',
                 'Central Nacional Unimed (CNU)', 'GreenLine Sistema de Saúde', 'Bradesco Seguros']

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

    return render(request, 'home.html', {'len': len(Paciente.objects.all()), 'porc_conv': porc_conv})
