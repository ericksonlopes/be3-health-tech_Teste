from django.db import models


# Create your models here.
from register_patient.choices import SEXO_CHOICES, CONVENIOS_CHOICES


class Paciente(models.Model):
    prontuario = models.CharField(max_length=50, verbose_name='Prontuário', blank=True, null=True)
    nome = models.CharField(max_length=100, verbose_name='Nome', blank=True, null=True)
    sobrenome = models.CharField(max_length=100, verbose_name='Sobrenome', blank=True, null=True)
    email = models.EmailField(verbose_name='Email', blank=True, null=True)
    data_nasci = models.DateField(auto_now_add=False, verbose_name='Data de Nascimento', blank=True, null=True)
    genero = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=True, null=True, verbose_name='Gênero')

    cpf = models.CharField(max_length=11, verbose_name='CPF', unique=True, blank=True, null=True)
    rg = models.CharField(max_length=11, verbose_name='CPF', unique=True, blank=True, null=True)
    uf_rg = models.IntegerField(verbose_name='UF do CPF', blank=True, null=True)

    celular = models.CharField(max_length=12, verbose_name='Nº telefone celular', blank=True, null=True)
    tel_fixo = models.CharField(max_length=12, verbose_name='Nº telefone fixo', blank=True, null=True)

    convenio = models.CharField(max_length=50, choices=CONVENIOS_CHOICES, blank=True, null=True, verbose_name='Convênio')
    carteira_convenio = models.IntegerField(verbose_name='Carteira convênio', blank=True, null=True)
    val_carteirinha = models.CharField(max_length=5, verbose_name='Validade Carteira', blank=True, null=True)

    def __str__(self):
        return str(self.nome) + '-' + str(self.sobrenome) + '-' + str(self.pk)
