from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import HealthInsurance


@login_required
def list_hi(request):
    return render(request, 'health_insurance/list_hi.html', {'hi': HealthInsurance.objects.all()})


@login_required
def create_hi(request):
    if request.method == 'GET':
        return render(request, 'health_insurance/create_hi.html')

    try:
        if request.POST:
            HealthInsurance.objects.create(
                name=request.POST['name']
            )
        return render(request, 'health_insurance/create_hi.html', {'save': 'Convênio salvo com sucesso'})
    except Exception as err:
        return render(request, 'health_insurance/create_hi.html', {'error': err})


def update_hi(request, pk):
    if request.method == 'GET':
        return render(request, 'health_insurance/update_hi.html', {'hi': HealthInsurance.objects.get(pk=pk)})

    try:
        if request.POST:
            HealthInsurance.objects.filter(pk=pk).update(
                name=request.POST['name'],
                status=request.POST['status']
            )
        return render(request, 'health_insurance/update_hi.html', {'save': 'Atualizado com sucesso',
                                                                   'hi': HealthInsurance.objects.get(pk=pk)})
    except Exception as err:
        return render(request, 'health_insurance/update_hi.html', {'error': err,
                                                                   'hi': HealthInsurance.objects.get(pk=pk)})
