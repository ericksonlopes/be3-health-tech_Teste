from django.shortcuts import render
from django.views.generic import ListView
from register_patient.models import Paciente
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from health_insurance.models import HealthInsurance


class PacienteViewCBV(LoginRequiredMixin, ListView):
    model = Paciente
    context_object_name = 'paciente'
    # Template especificado
    template_name = 'pacient/list_pac.html'


@login_required
def create_pac(request):
    if request.method == 'GET':
        return render(request, 'pacient/create_pac.html', {'conv': HealthInsurance.objects.all()})

    try:
        if Paciente.objects.filter(cpf=request.POST['cpf']):
            raise Exception('Este CPF ja existe no sistema!')

        if Paciente.objects.filter(cpf=request.POST['rg']):
            raise Exception('Este RG ja existe no sistema!')

        if request.POST['celular'].replace('_', '') or request.POST['tel_fixo'].replace('_', ''):
            pass
        else:
            raise Exception('Ao menos um dos campos entra telefone fixo e celular devem estar preenchido!')

        if request.POST:
            Paciente.objects.create(
                prontuario=request.POST['prontuario'],
                nome=request.POST['nome'],
                sobrenome=request.POST['sobrenome'],
                data_nasci=request.POST['data_nasci'],
                genero=request.POST['genero'],
                cpf=request.POST['cpf'],
                rg=request.POST['rg'],
                uf_rg=request.POST['uf_rg'],
                email=request.POST['email'],
                celular=request.POST['celular'].replace('_', ''),
                tel_fixo=request.POST['tel_fixo'].replace('_', ''),
                convenio=request.POST['convenio'],
                carteira_convenio=request.POST['carteira_convenio'],
                val_carteirinha=request.POST['val_carteirinha'],
            )
            return render(request, 'pacient/create_pac.html', {'save': 'Salvo com sucesso',
                                                               'conv': HealthInsurance.objects.all()})

    except Exception as err:
        return render(request, 'pacient/create_pac.html', {'error': err, 'conv': HealthInsurance.objects.all()})


@login_required
def update_pac(request, pk):
    if request.method == 'GET':
        return render(request, 'pacient/update_pac.html', {'pac': Paciente.objects.get(pk=pk),
                                                           'conv': HealthInsurance.objects.all()})

    else:
        try:
            if not Paciente.objects.filter(pk=pk, cpf=request.POST['cpf']) and \
                    Paciente.objects.filter(cpf=request.POST['cpf']):
                raise Exception('Este RG ja existe no sistema!')

            if not Paciente.objects.filter(pk=pk, cpf=request.POST['rg']) and \
                    Paciente.objects.filter(cpf=request.POST['rg']):
                raise Exception('Este RG ja existe no sistema!')

            if not request.POST['celular'].replace('_', '') or not request.POST['tel_fixo'].replace('_', ''):
                raise Exception('Ao menos um dos campos entra telefone fixo e celular devem estar preenchido!')

            Paciente.objects.filter(pk=pk).update(
                prontuario=request.POST['prontuario'],
                nome=request.POST['nome'],
                sobrenome=request.POST['sobrenome'],
                data_nasci=request.POST['data_nasci'],
                genero=request.POST['genero'],
                cpf=request.POST['cpf'],
                rg=request.POST['rg'],
                uf_rg=request.POST['uf_rg'],
                email=request.POST['email'],
                celular=request.POST['celular'].replace('_', ''),
                tel_fixo=request.POST['tel_fixo'].replace('_', ''),
                convenio=request.POST['convenio'],
                carteira_convenio=request.POST['carteira_convenio'],
                val_carteirinha=request.POST['val_carteirinha'],
            )
            return render(request, 'pacient/update_pac.html', {'save': 'Alteração Salva com sucesso',
                                                               'pac': Paciente.objects.get(pk=pk),
                                                               'conv': HealthInsurance.objects.all()})
        except Exception as err:
            return render(request, 'pacient/update_pac.html', {'error': f'Não foi possivel salvar o novo paciente, '
                                                                        f'Por favor, '
                                                                        f'tente novamente com as informações corretas. '
                                                                        f'{err}',
                                                               'pac': Paciente.objects.get(pk=pk),
                                                               'conv': HealthInsurance.objects.all()})
