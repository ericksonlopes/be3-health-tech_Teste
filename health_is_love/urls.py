from django.contrib import admin
from django.urls import path

from register_patient.views import PacienteViewCBV, teste_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', PacienteViewCBV.as_view())
    path('', teste_view)
]
