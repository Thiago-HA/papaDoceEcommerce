from multiprocessing import context
from django.shortcuts import HttpResponse, redirect, render
import mercadopago
from pedido.models import Pedido, Pedido_Produto
from usuarios.models import Endereco, Usuario, Usuario_endereco
from produto.models import Carrinho, Produto

def verifica_carrinho(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        usuariostr = str(usuario.id)

        carrinho = Carrinho.objects.filter(user_id = usuario.id)
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
        resposta = request.GET.get('resposta')

        endereco = Usuario_endereco.objects.filter(user = usuario.id)

        carrinho = Carrinho.objects.filter(user_id = usuario.pk)
        # carrinho = Produto.objects.raw('SELECT * FROM (produto_produto INNER JOIN produto_carrinho ON produto_produto.id = produto_carrinho.produto_id) INNER JOIN usuarios_usuario ON produto_carrinho.user_id = usuarios_usuario.id WHERE  produto_carrinho.user_id = %s;', [usuariostr])
        qtd_carrinho = len(carrinho)

        produtos = Carrinho.objects.filter(user = usuario)
        total = 0
        for produtos in produtos :
            precoo = produtos.produto.preco
            total = float(precoo) + total
            total = round(total, 2) # aparecer duas casas depois da virgula  

        
        
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
                ],
                "back_urls": {
                    "success": "http://127.0.0.1:8000/pedido/verifica_pagamento/",
                    "failure": "http://127.0.0.1:8000/pedido/verifica_pagamento/",
                }
                
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
            'endereco' : endereco,
        }
        return render(request, 'carrinho.html', context)
    else:
        return redirect('login')



def carrinho_add(request, id):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        produto = Produto.objects.get(id = id)
        carrinho = Carrinho.objects.filter(produto_id = produto.id , user_id = usuario.id) 

        
        carrinho_cadastro = Carrinho(user = usuario, produto = produto)
        carrinho_cadastro.save()## salva no banco de Dados
        return redirect('carrinho')

    else:
        return redirect('login')


def carrinho_remove(request, id):
    if request.session.get('usuario'):
        
        carrinho = Carrinho.objects.get(id = id)

        #se ele já ta na lista deleta:
        carrinho.delete()## deleta no banco de Dados
        return redirect('verifica_carrinho')


    else:
        return redirect('login')


## este é a mesma função de adicionar endereco da tela de perfil porem redirecona ao carrinho.
def endereco_add_carrinho(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        cep = request.POST.get('cep')
        complemento = request.POST.get('complemento')
        
        

        # if len(rua.strip()) == 0 or len(numero.strip()) == 0 or len(bairro.strip()) == 0 or len(cidade.strip()) == 0 or len(cep.strip()) == 0: 
        #     ##len() se refere ao tamanho e .strip() retira os espaços do inicio e do final.
        #     return redirect('/produto/endereco_entrega/?resposta=2')

        try:
            endereco = Endereco(rua = rua, numero = numero, bairro = bairro, cidade= cidade, cep = cep, complemento = complemento)
            endereco.save()

            usuario_endereco = Usuario_endereco(user_id = usuario.id, endereco_id = endereco.id)
            usuario_endereco.save()

            return redirect('/produto/endereco_entrega/')
        except:
            return redirect('/produto/endereco_entrega/?resposta=1')

    else:
        return redirect('login')



## ENDEREÇO DE ENTREGA:

def endereco_entrega(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        usuariostr = str(usuario.id)
        status = request.GET.get('status')
        resposta = request.GET.get('resposta')

        endereco = Usuario_endereco.objects.filter(user = usuario.id)

        carrinho = Carrinho.objects.filter(user_id = usuario.id)
        # carrinho = Produto.objects.raw('SELECT * FROM (produto_produto INNER JOIN produto_carrinho ON produto_produto.id = produto_carrinho.produto_id) INNER JOIN usuarios_usuario ON produto_carrinho.user_id = usuarios_usuario.id WHERE  produto_carrinho.user_id = %s;', [usuariostr])
        qtd_carrinho = len(carrinho)

        produtos = Carrinho.objects.filter(user = usuario)
        total = 0
        for produtos in produtos :
            precoo = produtos.produto.preco
            total = float(precoo) + total
            total = round(total, 2) # aparecer duas casas depois da virgula  
        
        
        context = {
            'carrinho' : carrinho,
            'status' : status,
            'usuario' : usuario,
            'total' : total,
            'endereco' : endereco,
            'resposta':resposta,
        }
        return render(request, 'endereco_entrega.html', context)
    else:
        return redirect('login')


def carrinho_remove_endereco(request, id):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])

        carrinho = Carrinho.objects.get(id = id)

        carrinho.delete()## deleta no banco de Dados

        return redirect('endereco_entrega')

    else:
        return redirect('login')


## PAGAMENTO:

def pagamento(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        endereco_id = request.POST.get('endereco')
        carrinho = Carrinho.objects.filter(user_id = usuario.id)

        endereco = Endereco.objects.get(id = endereco_id)

        produtos = Carrinho.objects.filter(user = usuario)
        total = 0
        for produtos in produtos :
            precoo = produtos.produto.preco
            total = float(precoo) + total
            total = round(total, 2) # aparecer duas casas depois da virgula  
            
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
                ],
                "back_urls": {
                    "success": "http://127.0.0.1:8000/pedido/verifica_pagamento/?endereco="+ endereco_id,
                    "failure": "http://127.0.0.1:8000/pedido/verifica_pagamento/",
                }
                
            }
            

            # Cria a preferência
            preference_response = sdk.preference().create(preference_data)
            preference = preference_response["response"]
            preference = preference["id"]

        else:
           preference = "False"
        
        context = {
            'usuario' : usuario,
            'total' : total,
            'endereco' : endereco,
            'carrinho':carrinho,
            'preference':preference,
        }

        return render(request, 'pagamento.html', context)

    else:
        return redirect('login')
