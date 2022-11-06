
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


    

        
    
