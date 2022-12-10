from django.contrib import admin
from pedido.models import Pedido_Produto, Pedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    readonly_fields = ('data_emissao', 'id_cliente', 'rua', 'numero', 'bairro', 'cidade', 'cep','complemento', 'total' )

admin.site.register(Pedido_Produto)
