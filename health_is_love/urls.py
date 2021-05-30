from django.contrib import admin
from django.urls import path

from register_patient.views import PacienteViewCBV, teste_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', teste_view),
    path('list/', PacienteViewCBV.as_view()),
    # path('edit/', PacienteViewCBV.as_view())
]
