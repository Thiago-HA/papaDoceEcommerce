from multiprocessing import context
from django.shortcuts import redirect, render
from produto.models import Favorito, Produto
from usuarios.models import Usuario

def favoritos(request):
    if request.session.get('usuario'):
        status = request.GET.get('status')
        fav = Produto.objects.raw('SELECT * FROM (produto_produto INNER JOIN produto_favorito ON produto_produto.id = produto_favorito.prod_id) INNER JOIN usuarios_usuario ON produto_favorito.user_id = usuarios_usuario.id;')
        
        context = {
            'fav' : fav,
            'status' : status
        }
        return render(request, 'favoritos.html', context)
    else:
        return redirect('login')

def verifica_favoritos(request):
    if request.session.get('usuario'):
        fav = Produto.objects.raw('SELECT * FROM (produto_produto INNER JOIN produto_favorito ON produto_produto.id = produto_favorito.prod_id) INNER JOIN usuarios_usuario ON produto_favorito.user_id = usuarios_usuario.id;')
        if fav:
            return redirect('favoritos')
        else:
            return redirect('/minha_conta/favoritos/?status=1')

    else:
        return redirect('login')
