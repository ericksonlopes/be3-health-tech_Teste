from django.views.generic import ListView
from register_patient.models import Paciente


class PacienteViewCBV(ListView):
    model = Paciente
    context_object_name = 'paciente'
    # Template especificado
    template_name = 'listview.html'
