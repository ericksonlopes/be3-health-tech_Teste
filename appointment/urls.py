from django.urls import path
from .views import list_appo, create_appo, update_appo

urlpatterns = [
    path('list_appo/', list_appo, name='list-appo'),
    path('add-appo/<int:pk>', create_appo, name='create-appo'),
    path('editar-appo/<int:pk>', update_appo, name='update-appo'),
]
