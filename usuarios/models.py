
from datetime import date
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    apelido = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField( null=False, blank=False)
    senha = models.CharField(max_length=64, null=False, blank=False)
    cpf = models.CharField( max_length=18, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    rua = models.CharField(max_length=100, null=False, blank=False)
    numero = models.CharField( max_length=15)
    bairro = models.CharField( max_length=30, null=False, blank=False)
    cidade = models.CharField( max_length=30, null=False, blank=False)
    cep = models.CharField( max_length=10, null=False, blank=False)
    complemento = models.CharField( max_length=100)

    def __str__(self):
        return self.cidade

class Usuario_endereco(models.Model):
    user = models.ForeignKey(Usuario, null=True, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, null=True, on_delete=models.CASCADE)

    

        
    
