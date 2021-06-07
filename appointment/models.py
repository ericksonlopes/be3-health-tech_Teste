from django.db import models
from register_patient.models import Paciente


class Appointment(models.Model):
    pacient = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    doctorName = models.CharField(max_length=50)
