
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    full_name = models.CharField('Nome completo', max_length=255)
    telefone_number = models.CharField('Telefone celular', max_length=20)
    
    def __str__(self):
        return str(self.full_name)


class BusinessProfile(models.Model):
    name = models.CharField('Razão Social', max_length=255)
    address = models.CharField('Endereço', max_length=255)
    ceo = models.OneToOneField(User, on_delete=models.CASCADE, related_name='CEO_PJ')
    employees = models.ManyToManyField(User, related_name='Colaboradores')

    def __str__(self):
        return str(self.name)

