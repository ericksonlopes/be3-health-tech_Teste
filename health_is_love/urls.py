from django.contrib import admin
from django.urls import path

from register_patient.views import PacienteViewCBV, create_paciente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listagem/', PacienteViewCBV.as_view()),
    path('novo/', create_paciente),
    # path('adicionar/', PacienteAddCBV.as_view())
]
