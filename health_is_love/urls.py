from django.contrib import admin
from django.urls import path

from register_patient.views import PacienteViewCBV, create_pac, update_pac

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listagem/', PacienteViewCBV.as_view(), name='list'),
    path('novo/', create_pac, name='create'),
    path('editar/<int:pk>', update_pac, name='update'),
]
