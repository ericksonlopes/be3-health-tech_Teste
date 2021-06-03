from django.contrib import admin
from django.urls import path, include
from register_patient.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', homepage, name='home'),
    path('', include('register_patient.urls'))
]
