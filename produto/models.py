from distutils.command.upload import upload
from email.policy import default
import imp
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import date

class Produto(models.Model):
    titulo = models.CharField(max_length=300)
    imagem = models.ImageField(upload_to='img_produto', null=True, blank=True)
    favorito = models.BooleanField(default=False)
    descricao = models.CharField(max_length=1000, blank=True, null=True)
    marca = models.CharField(max_length=80, blank=True, null=True)
    preco = models.FloatField()
    cor = models.CharField(max_length=50, blank=True, null=True)
    disponivel = models.BooleanField(default=True)
    data_utm_alteracao = models.DateField(auto_now=True)
    data_cadastro = models.DateField(default= date.today)

    class Meta:
        verbose_name = 'Produto'

    def __str__(self) -> str:
        return self.titulo