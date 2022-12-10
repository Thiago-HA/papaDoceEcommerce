from django.db import models
from produto.models import Produto
from usuarios.models import Endereco, Usuario


class Pedido(models.Model):
    data_emissao = models.DateField(auto_now_add=True)
    id_cliente = models.ForeignKey(Usuario, verbose_name='Cliente', on_delete=models.DO_NOTHING)
    rua = models.CharField(max_length=100, null=False, blank=False)
    numero = models.CharField( max_length=15 )
    bairro = models.CharField( max_length=30, null=False, blank=False)
    cidade = models.CharField( max_length=30, null=False, blank=False)
    cep = models.CharField( max_length=10, null=False, blank=False)
    complemento = models.CharField( max_length=100)
    total = models.DecimalField("Total", max_digits=8, decimal_places=2)



    class Meta:
        verbose_name = 'Pedido'

    def __int__(self) -> str:
        return self.id_cliente

class Pedido_Produto(models.Model):
    pedido_id = models.ForeignKey(Pedido, null=True, on_delete=models.CASCADE)
    produto_id = models.ForeignKey(Produto, null=True, on_delete=models.CASCADE)
    