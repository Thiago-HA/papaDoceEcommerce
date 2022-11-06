from distutils.command.upload import upload
from email.policy import default
import imp
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import date
from usuarios.models import Usuario

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()

    def __str__(self) -> str:
        return self.nome
    
class Produto(models.Model):
    titulo = models.CharField(max_length=300)
    imagem = models.ImageField(upload_to='img_produto', null=False, blank=False,)
    descricao = models.CharField(max_length=1000, blank=True, null=True)
    marca = models.CharField(max_length=80, blank=True, null=True)
    preco = models.FloatField()
    cor = models.CharField(max_length=50, blank=True, null=True)
    disponivel = models.BooleanField(default=True)
    data_utm_alteracao = models.DateField(auto_now=True)
    data_cadastro = models.DateField(default= date.today)
    estoque = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)


    class Meta:
        verbose_name = 'Produto'

    def __str__(self) -> str:
        return self.titulo
class Carrinho(models.Model):
    user = models.ForeignKey(Usuario, null=True, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, null=True, on_delete=models.CASCADE)

class Favorito(models.Model):
    user = models.ForeignKey(Usuario, null=True, on_delete=models.CASCADE)
    prod = models.ForeignKey(Produto, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.prod
