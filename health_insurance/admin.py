from django.contrib import admin
from health_insurance.models import HealthInsurance


@admin.register(HealthInsurance)
class HealthInsuranceAdmin(admin.ModelAdmin):
    list_display = ['name']
