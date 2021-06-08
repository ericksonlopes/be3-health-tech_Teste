from django.urls import path
from .views import list_dc, create_dc, update_dc

urlpatterns = [
    path('list-dc/', list_dc, name='list-dc'),
    path('create-dc/', create_dc, name='create-dc'),
    path('update-dc/<int:pk>', update_dc, name='update-dc'),
]


