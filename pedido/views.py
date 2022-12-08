from django.shortcuts import redirect, render

# SDK do Mercado Pago
import mercadopago
from pedido.models import Pedido
from produto.models import Produto

from usuarios.models import Usuario


def verifica_pagamento(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        usuariostr = str(usuario.id)
        
        carrinho = Produto.objects.raw('SELECT * FROM (produto_produto INNER JOIN produto_carrinho ON produto_produto.id = produto_carrinho.produto_id) INNER JOIN usuarios_usuario ON produto_carrinho.user_id = usuarios_usuario.id WHERE  produto_carrinho.user_id = %s;', [usuariostr])
        qtd_carrinho = len(carrinho)


        #carregar os dados da quantdade da lista de favoritos:
        fav = Produto.objects.raw('SELECT * FROM (produto_produto INNER JOIN produto_favorito ON produto_produto.id = produto_favorito.prod_id) INNER JOIN usuarios_usuario ON produto_favorito.user_id = usuarios_usuario.id WHERE  produto_favorito.user_id = %s;', [usuariostr])
        qtd_favoritos = len(fav)

        payment = request.GET.get('payment_id')
        status = request.GET.get('status')
        payment_type = request.GET.get('payment_type')
        order_id = request.GET.get('merchant_order_id')

        # if status == 'approved':
        #     pedido = Pedido()

        context = {
            'carrinho' : carrinho,
            'qtd_carrinho' : qtd_carrinho,
            'qtd_favoritos' : qtd_favoritos,
            'usuario' : usuario,
            'payment' : payment,
            'status' : status,
            'payment_type' : payment_type,
            'order_id' : order_id,

        }
        return render(request, 'verifica_pagamento.html', context)
    else:
        return redirect('login')

