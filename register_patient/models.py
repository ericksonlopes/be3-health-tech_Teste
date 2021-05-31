from django.db import models


# Create your models here.
from register_patient.choices import SEXO_CHOICES, CONVENIOS_CHOICES


class Paciente(models.Model):
    prontuario = models.IntegerField(verbose_name='Prontuário')
    nome = models.CharField(max_length=100, verbose_name='Nome')
    sobrenome = models.CharField(max_length=100, verbose_name='Sobrenome')
    email = models.EmailField(verbose_name='Email')
    data_nasci = models.DateField(auto_now_add=False, verbose_name='Data de Nascimento')
    genero = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False, verbose_name='Gênero')

    cpf = models.CharField(max_length=11, verbose_name='CPF', unique=True)
    rg = models.CharField(max_length=11, verbose_name='CPF', unique=True)
    uf_rg = models.IntegerField(verbose_name='UF do CPF')

    celular = models.CharField(max_length=12, unique=True, verbose_name='Nº telefone celular')
    tel_fixo = models.CharField(max_length=12, verbose_name='Nº telefone fixo')

    convenio = models.CharField(max_length=50, choices=CONVENIOS_CHOICES, blank=False, null=False, verbose_name='Convênio')
    carteira_convenio = models.IntegerField(verbose_name='Carteira convênio')
    val_carteirinha = models.CharField(max_length=5, verbose_name='Validade Carteira')

    def __str__(self):
        return str(self.nome) + str(self.sobrenome)
