from django.urls import path
from .views import list_hi, create_hi, update_hi

urlpatterns = [
    path('list-hi/', list_hi, name='list-hi'),
    path('create-hi/', create_hi, name='create-hi'),
    path('update-hi/<int:pk>', update_hi, name='update-hi'),
]


