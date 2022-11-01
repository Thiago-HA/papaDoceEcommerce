from multiprocessing import context
from django.shortcuts import HttpResponse, redirect, render
from usuarios.models import Usuario
from produto.models import Carrinho, Produto

def verifica_carrinho(request):
    if request.session.get('usuario'):
        carrinho = Produto.objects.raw('SELECT * FROM (produto_produto INNER JOIN produto_carrinho ON produto_produto.id = produto_carrinho.produto_id) INNER JOIN usuarios_usuario ON produto_carrinho.user_id = usuarios_usuario.id;')
        if carrinho:
            return redirect('carrinho')
        else:
            return redirect('/produto/meu_carrinho/?status=1')

    else:
        return redirect('login')

def carrinho(request):
    if request.session.get('usuario'):
        status = request.GET.get('status')
        carrinho = Produto.objects.raw('SELECT * FROM (produto_produto INNER JOIN produto_carrinho ON produto_produto.id = produto_carrinho.produto_id) INNER JOIN usuarios_usuario ON produto_carrinho.user_id = usuarios_usuario.id;')
        qtd_carrinho = len(carrinho)

        #carregar os dados da quantdade da lista de favoritos:
        fav = Produto.objects.raw('SELECT * FROM (produto_produto INNER JOIN produto_favorito ON produto_produto.id = produto_favorito.prod_id) INNER JOIN usuarios_usuario ON produto_favorito.user_id = usuarios_usuario.id;')
        qtd_favoritos = len(fav)

        context = {
            'carrinho' : carrinho,
            'status' : status,
            'qtd_carrinho' : qtd_carrinho,
            'qtd_favoritos' : qtd_favoritos,
        }
        return render(request, 'carrinho.html', context)
    else:
        return redirect('login')


def carrinho_add(request, id):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        produto = Produto.objects.get(id = id)
        carrinho = Carrinho.objects.filter(produto_id = produto.id)

        if carrinho:

            return redirect('home')
        else:
            carrinho_cadastro = Carrinho(user = usuario, produto = produto)
            carrinho_cadastro.save()## salva no banco de Dados
            return redirect('carrinho')

    else:
        return redirect('login')


def carrinho_remove(request, id):
    if request.session.get('usuario'):
        produto = Produto.objects.get(id = id)
        carrinho = Carrinho.objects.filter(produto_id = produto.id)

        #se ele já ta na lista deleta:
        if carrinho:
            carrinho.delete()## deleta no banco de Dados
            return redirect('verifica_carrinho')

    else:
        return redirect('login')