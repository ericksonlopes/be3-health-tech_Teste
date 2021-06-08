from django.urls import path

from .views import list_hi

urlpatterns = [
    path('list-hi/', list_hi, name='list-hi'),
]


