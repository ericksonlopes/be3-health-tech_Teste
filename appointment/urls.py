from django.urls import path
from .views import list_appo

urlpatterns = [
    path('list_appo/', list_appo, name='list-appo'),
]
