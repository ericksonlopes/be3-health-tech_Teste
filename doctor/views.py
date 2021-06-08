from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Doctor


@login_required
def list_dc(request):
    return render(request, 'doctor/list_dc.html', {'dc': Doctor.objects.all()})


@login_required
def create_dc(request):
    if request.method == 'GET':
        return render(request, 'doctor/create_dc.html')

    try:
        if request.POST:
            Doctor.objects.create(
                name=request.POST['name'],
                crm=request.POST['crm']
            )
        return render(request, 'doctor/create_dc.html', {'save': 'Doutor salvo com sucesso'})
    except Exception as err:
        return render(request, 'doctor/create_dc.html', {'error': err})


def update_dc(request, pk):
    if request.method == 'GET':
        return render(request, 'doctor/update_dc.html', {'dc': Doctor.objects.get(pk=pk)})

    try:
        if request.POST:
            Doctor.objects.filter(pk=pk).update(
                name=request.POST['name'],
                crm=request.POST['crm']
            )
        return render(request, 'doctor/update_dc.html', {'save': 'Atualizado com sucesso',
                                                         'dc': Doctor.objects.get(pk=pk)})
    except Exception as err:
        return render(request, 'doctor/update_dc.html', {'error': err,
                                                         'dc': Doctor.objects.get(pk=pk)})
