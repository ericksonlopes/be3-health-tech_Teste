from django.db import models


class HealthInsurance(models.Model):
    name = models.CharField(max_length=100)
