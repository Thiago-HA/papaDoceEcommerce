from django.shortcuts import redirect, render

# SDK do Mercado Pago
import mercadopago
from pedido.models import Pedido
from produto.models import Produto

from usuarios.models import Usuario


# def pedido(request):
#     if request.session.get('usuario'):
#         usuario = Usuario.objects.get(id = request.session['usuario'])
#         usuariostr = str(usuario.id)
        
#         carrinho = Produto.objects.raw('SELECT * FROM (produto_produto INNER JOIN produto_carrinho ON produto_produto.id = produto_carrinho.produto_id) INNER JOIN usuarios_usuario ON produto_carrinho.user_id = usuarios_usuario.id WHERE  produto_carrinho.user_id = %s;', [usuariostr])
#         qtd_carrinho = len(carrinho)


#         #carregar os dados da quantdade da lista de favoritos:
#         fav = Produto.objects.raw('SELECT * FROM (produto_produto INNER JOIN produto_favorito ON produto_produto.id = produto_favorito.prod_id) INNER JOIN usuarios_usuario ON produto_favorito.user_id = usuarios_usuario.id WHERE  produto_favorito.user_id = %s;', [usuariostr])
#         qtd_favoritos = len(fav)

#         context = {
#             'carrinho' : carrinho,
#             'qtd_carrinho' : qtd_carrinho,
#             'qtd_favoritos' : qtd_favoritos,
#             'usuario' : usuario,
#         }
#         return render(request, 'pedido.html', context)
#     else:
#         return redirect('login')


# def finalizar_pedido(request):
#     if request.session.get('usuario'):
        
        
#         return render(request, 'finalizarPedido.html')

#     else:
#         return redirect('login')

