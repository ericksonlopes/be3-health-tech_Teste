from django.contrib import admin
from register_patient.models import Paciente


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome', 'data_nasci', 'genero', 'cpf', 'email', 'celular']
