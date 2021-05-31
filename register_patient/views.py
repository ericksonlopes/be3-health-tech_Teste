from django.shortcuts import render
from django.views.generic import ListView
from register_patient.models import Paciente


class PacienteViewCBV(ListView):
    model = Paciente
    context_object_name = 'paciente'
    # Template especificado
    template_name = 'list_pac.html'


def create_paciente(request):
    if request.POST:
        PacienteViewCBV.objects.create(
            prontuario=request.POST['prontuario'],
            nome=request.POST['nome'],
            sobrenome=request.POST['sobrenome'],
            data_nasci=request.POST['data_nasci'],
            genero=request.POST['genero'],
            cpf=request.POST['cpf'],
            uf_rg=request.POST['uf_rg'],
            email=request.POST['email'],
            celular=request.POST['celular'],
            tel_fixo=request.POST['tel_fixo'],
            convenio=request.POST['convenio'],
            carteira_convenio=request.POST['carteira_convenio'],
            val_carteirinha=request.POST[' val_carteirinha'],
        )
        return render(request, 'create_pac.html')
