from django.urls import path

from .views import PacienteViewCBV, create_pac, update_pac

urlpatterns = [
    path('list-pac/', PacienteViewCBV.as_view(), name='list-pac'),
    path('add-pac/', create_pac, name='create-pac'),
    path('edit-pac/<int:pk>', update_pac, name='update-pac'),
]


