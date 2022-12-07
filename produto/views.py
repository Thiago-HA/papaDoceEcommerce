from multiprocessing import context
from django.shortcuts import HttpResponse, redirect, render
import mercadopago
from usuarios.models import Usuario
from produto.models import Carrinho, Produto

def verifica_carrinho(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        usuariostr = str(usuario.id)

        carrinho = Produto.objects.raw('SELECT * FROM (produto_produto INNER JOIN produto_carrinho ON produto_produto.id = produto_carrinho.produto_id) INNER JOIN usuarios_usuario ON produto_carrinho.user_id = %s;', [usuariostr])
        if carrinho:
            return redirect('carrinho')
        else:
            return redirect('/produto/meu_carrinho/?status=1')
 
    else:
        return redirect('login')

def carrinho(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        usuariostr = str(usuario.id)
        status = request.GET.get('status')

        carrinho = Produto.objects.raw('SELECT * FROM (produto_produto INNER JOIN produto_carrinho ON produto_produto.id = produto_carrinho.produto_id) INNER JOIN usuarios_usuario ON produto_carrinho.user_id = usuarios_usuario.id WHERE  produto_carrinho.user_id = %s;', [usuariostr])
        qtd_carrinho = len(carrinho)

        produtos = Carrinho.objects.filter(user = usuario)
        total = 0
        for produtos in produtos :
            precoo = produtos.produto.preco
            total= float(precoo) + total

        
        
        #total = Produto.objects.raw('SELECT SUM(preco) FROM (produto_produto INNER JOIN produto_carrinho ON produto_produto.id = produto_carrinho.produto_id) INNER JOIN usuarios_usuario ON produto_carrinho.user_id = usuarios_usuario.id WHERE  produto_carrinho.user_id = %s;', [usuariostr])

        #carregar os dados da quantdade da lista de favoritos:
        fav = Produto.objects.raw('SELECT * FROM (produto_produto INNER JOIN produto_favorito ON produto_produto.id = produto_favorito.prod_id) INNER JOIN usuarios_usuario ON produto_favorito.user_id = usuarios_usuario.id WHERE  produto_favorito.user_id = %s;', [usuariostr])
        qtd_favoritos = len(fav)


        if carrinho:
             # Adicione as credenciais
            sdk = mercadopago.SDK("TEST-7206970217417319-112923-f38efa38057699afb94cdd1073d179c1-221366732")
            
            # Cria um item na preferência
            preference_data = {
                "items": [
                    {
                        "title": "Produtos",
                        "quantity": 1,
                        "unit_price": total
                    },
                ]
            }

            # Cria a preferência
            preference_response = sdk.preference().create(preference_data)
            preference = preference_response["response"]
            preference = preference["id"]
        else:
           preference = "False"

        context = {
            'carrinho' : carrinho,
            'status' : status,
            'qtd_carrinho' : qtd_carrinho,
            'qtd_favoritos' : qtd_favoritos,
            'usuario' : usuario,
            'preference' : preference,
            'total' : total,
        }
        return render(request, 'carrinho.html', context)
    else:
        return redirect('login')



def carrinho_add(request, id):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        produto = Produto.objects.get(id = id)
        carrinho = Carrinho.objects.filter(produto_id = produto.id , user_id = usuario.id) 

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
        usuario = Usuario.objects.get(id = request.session['usuario'])
        produto = Produto.objects.get(id = id)
        carrinho = Carrinho.objects.filter(produto_id = produto.id , user_id = usuario.id)

        #se ele já ta na lista deleta:
        if carrinho:
            carrinho.delete()## deleta no banco de Dados
            return redirect('verifica_carrinho')


    else:
        return redirect('login')
