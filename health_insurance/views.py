from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import HealthInsurance


@login_required
def list_hi(request):
    return render(request, 'health_insurance/list_hi.html', {'hi': HealthInsurance.objects.all()})
