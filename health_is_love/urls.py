from django.contrib import admin
from django.urls import path

from register_patient.views import PacienteViewCBV

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PacienteViewCBV.as_view())
]