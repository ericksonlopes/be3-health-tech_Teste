from django.contrib import admin
from django.urls import path, include
from .views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),

    # apps
    path('', include('django.contrib.auth.urls')),
    path('', include('register_patient.urls')),
    path('', include('health_insurance.urls')),
    path('', include('appointment.urls'))
]
