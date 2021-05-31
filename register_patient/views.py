from django.shortcuts import render
from django.views.generic import ListView
from register_patient.models import Paciente


class PacienteViewCBV(ListView):
    model = Paciente
    context_object_name = 'paciente'
    # Template especificado
    template_name = 'list_pac.html'


def create_pac(request):
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
            return render(request, 'create_pac.html', {'save': 'Salvo com sucesso'})

    except Exception as err:
        return render(request, 'create_pac.html', {'error': err})

    return render(request, 'create_pac.html')


def update_pac(request, pk):
    if request.method == 'GET':
        return render(request, 'update_pac.html', {'pac': Paciente.objects.get(pk=pk)})

    else:
        try:
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
            return render(request, 'update_pac.html', {'save': 'Alteração Salva com sucesso',
                                                       'pac': Paciente.objects.get(pk=pk)})
        except Exception as err:
            return render(request, 'update_pac.html', {'error': f'Não foi possivel salvar o novo paciente, Por favor, '
                                                                f'tente novamente com as informações corretas. {err}',
                                                       'pac': Paciente.objects.get(pk=pk)})


