from django.db import models
from produto.models import Produto
from usuarios.models import Endereco, Usuario


class Pedido(models.Model):
    data_emissao = models.DateField(auto_now_add=True)
    id_cliente = models.ForeignKey(Usuario, verbose_name='Cliente', on_delete=models.DO_NOTHING)


    class Meta:
        verbose_name = 'Pedido'

    def __str__(self) -> str:
        return self.id_cliente

class Pedido_Produto(models.Model):
    pedido_id = models.ForeignKey(Pedido, null=True, on_delete=models.CASCADE)
    produto_id = models.ForeignKey(Produto, null=True, on_delete=models.CASCADE)

    