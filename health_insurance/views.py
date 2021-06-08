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
