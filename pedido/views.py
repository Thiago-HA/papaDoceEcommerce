from django.shortcuts import redirect, render

# SDK do Mercado Pago
import mercadopago
from pedido.models import Pedido, Pedido_Produto
from produto.models import Carrinho, Produto

from usuarios.models import Endereco, Usuario



def verifica_pagamento(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        usuariostr = str(usuario.id)
        endereco_id = request.GET.get('endereco')
        
        carrinho = Carrinho.objects.filter(user_id = usuario.pk)
        qtd_carrinho = len(carrinho)

        endereco = Endereco.objects.get(id = endereco_id)

        produtos = Carrinho.objects.filter(user = usuario)
        total = 0
        for produtos in produtos :
            precoo = produtos.produto.preco
            total = float(precoo) + total
            total = round(total, 2) # aparecer duas casas depois da virgula  


        #carregar os dados da quantdade da lista de favoritos:
        fav = Produto.objects.raw('SELECT * FROM (produto_produto INNER JOIN produto_favorito ON produto_produto.id = produto_favorito.prod_id) INNER JOIN usuarios_usuario ON produto_favorito.user_id = usuarios_usuario.id WHERE  produto_favorito.user_id = %s;', [usuariostr])
        qtd_favoritos = len(fav)

        payment = request.GET.get('payment_id')
        status = request.GET.get('status')
        payment_type = request.GET.get('payment_type')
        order_id = request.GET.get('merchant_order_id')

        context = {
            'qtd_favoritos' : qtd_favoritos,
            'usuario' : usuario,
            'payment' : payment,
            'status' : status,
            'payment_type' : payment_type,
            'order_id' : order_id,
            'total':total,

        }


        #CRIAÇÃO DO PEDIDO:
        if status == 'approved':
            try:
                pedido = Pedido(id_cliente_id= usuario.id, bairro= endereco.bairro, cep= endereco.cep ,cidade= endereco.cidade, complemento= endereco.complemento, numero= endereco.numero, rua= endereco.rua, total= total)
                pedido.save()
                
                produtos_ = Carrinho.objects.filter(user = usuario)
                for produtos_ in produtos_ :
                    id= produtos_.produto.pk
                    produtos_pedido = Pedido_Produto(pedido_id_id = pedido.id , produto_id_id = id)
                    produtos_pedido.save()

                carrinho.delete()

                return render(request, 'verifica_pagamento.html', context)
            except:
                return redirect('/produto/endereco_entrega/?resposta=1')
        
    else:
        return redirect('login')

def meus_pedidos(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        usuariostr = str(usuario.id)
        status = request.GET.get('status')

        carrinho = Carrinho.objects.filter(user_id = usuario.pk)
        qtd_carrinho = len(carrinho)

        pedidos = Pedido.objects.filter(id_cliente_id = usuario.pk)
        # pedido_produto = Pedido_Produto.objects.all()
        
        produto_pedido = Pedido_Produto.objects.raw('SELECT * FROM (pedido_pedido_produto INNER JOIN pedido_pedido ON pedido_pedido.id = pedido_pedido_produto.pedido_id_id) INNER JOIN usuarios_usuario ON usuarios_usuario.id = pedido_pedido.id_cliente_id WHERE  usuarios_usuario.id = %s group by pedido_pedido_produto.pedido_id_id;', [usuariostr])
        
        #fazer outro raw :
        #um para pegar os produtos e outro para pegar os enderecos (todos com filtro de usuario)
            

        #carregar os dados da quantdade da lista de favoritos:
        fav = Produto.objects.raw('SELECT * FROM (produto_produto INNER JOIN produto_favorito ON produto_produto.id = produto_favorito.prod_id) INNER JOIN usuarios_usuario ON produto_favorito.user_id = usuarios_usuario.id WHERE  produto_favorito.user_id = %s;', [usuariostr])
        qtd_favoritos = len(fav)

        context = {
            'qtd_favoritos' : qtd_favoritos,
            'qtd_carrinho' : qtd_carrinho,
            'usuario' : usuario,
            'pedidos' : pedidos,
            'status':status,
            'produto_pedido' : produto_pedido,
        }
        
        return render(request, 'pedidos.html', context)

    else:
        return redirect('login')

def verifica_meus_pedidos(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])

        pedidos = Pedido.objects.filter(id_cliente_id = usuario.pk)
        if pedidos:
            return redirect('/pedido/meus_pedidos/')
        else:
            return redirect('/pedido/meus_pedidos/?status=1')

    else:
        return redirect('login')




    