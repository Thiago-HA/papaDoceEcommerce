from django.shortcuts import HttpResponse, redirect, render
from usuarios.models import Usuario
from produto.models import Favorito, Produto, Categoria

# Create your views here.
def pagina_home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        usuariostr = str(usuario.id)
        produtos = Produto.objects.all() ## mostra todos os produtos.
        categorias = Categoria.objects.all()
        favoritos = Favorito.objects.raw('SELECT * FROM produto_favorito WHERE user_id = %s ', [usuario.id])

        #carregar a quantidade na lista de favoritos:
        fav = Produto.objects.raw('SELECT * FROM (produto_produto INNER JOIN produto_favorito ON produto_produto.id = produto_favorito.prod_id) INNER JOIN usuarios_usuario ON produto_favorito.user_id = usuarios_usuario.id WHERE  produto_favorito.user_id = %s;', [usuariostr])
        qtd_favoritos = len(fav)

        #carregar a quantidade na lista de Carrinho:
        carrinho = Produto.objects.raw('SELECT * FROM (produto_produto INNER JOIN produto_carrinho ON produto_produto.id = produto_carrinho.produto_id) INNER JOIN usuarios_usuario ON produto_carrinho.user_id = usuarios_usuario.id WHERE  produto_carrinho.user_id = %s;', [usuariostr])
        qtd_carrinho = len(carrinho)


        context = {
            'categorias': categorias,
            'produtos': produtos,
            'favorito' : favoritos,
            'qtd_favoritos' : qtd_favoritos,
            'qtd_carrinho' : qtd_carrinho,
        }

        return render(request, 'home_autenticado.html', context)
    else:
        produto = Produto.objects.all() ## mostra todos os produtos.
        return render(request, 'home.html', {'produtos': produto})

def ver_produto(request, id):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        usuariostr = str(usuario.id)
        produto = Produto.objects.get(id = id)

        #carregar a quantidade na lista de favoritos:
        fav = Produto.objects.raw('SELECT * FROM (produto_produto INNER JOIN produto_favorito ON produto_produto.id = produto_favorito.prod_id) INNER JOIN usuarios_usuario ON produto_favorito.user_id = usuarios_usuario.id WHERE  produto_favorito.user_id = %s;', [usuariostr])
        qtd_favoritos = len(fav)

        #carregar a quantidade na lista de Carrinho:
        carrinho = Produto.objects.raw('SELECT * FROM (produto_produto INNER JOIN produto_carrinho ON produto_produto.id = produto_carrinho.produto_id) INNER JOIN usuarios_usuario ON produto_carrinho.user_id = usuarios_usuario.id WHERE  produto_carrinho.user_id = %s;', [usuariostr])
        qtd_carrinho = len(carrinho)

        context = {
            'produto' : produto,
            'qtd_favoritos': qtd_favoritos,
            'qtd_carrinho': qtd_carrinho,
        }

        return render(request, 'ver_produto_autenticado.html', context)
    else:
        return render(request,'ver_produto.html')

def filtrar(request):
    
    if request.session.get('usuario'):
        categorias = Categoria.objects.all()
        
        queryAND=''
        for i in categorias:
            id = str(i.id)
            categ_selected = request.POST.get(id)
            if categ_selected == id:
                produtos = Produto.objects.raw('SELECT * FROM produto_produto WHERE categoria_id = %s', [id])
            else:
                print('teste')
        
        context = {
            'categorias': categorias,
            'prods': produtos,
        }

        print(context)
        #query = 'SELECT * FROM produto_produto WHERE categoria_id = %s %s' % categ_selected % queryAND
        


            


        #for i in categorias:
            #id_ceteg = i.id
            #id_ceteg = str(id_ceteg)
            #categ_selection = request.POST.get(id_ceteg)
            #if categ_selection == 'on':
                #produtos = Produto.objects.raw('SELECT * FROM produto_produto WHERE categoria_id = "%" ', [id_ceteg])
                #produtos = Produto.objects.filter(categoria = cat)
                

        return render(request, 'home_autenticado_filtrado.html', context)
    else:
        return render(request,'')

def favoritos_add(request, id):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        produto = Produto.objects.get(id = id)
        fav = Favorito.objects.filter(prod_id = produto.id , user_id = usuario.id)

        #se ele já ta na lista deleta, e se não, adiciona: 
        if fav:
            return redirect('home')
        else:
            favorito = Favorito(user = usuario, prod = produto)
            favorito.save()## salva no banco de Dados
            return redirect('home')

    else:
        return redirect('login')

def favoritos_remove(request, id):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        produto = Produto.objects.get(id = id)
        fav = Favorito.objects.filter(prod_id = produto.id ,  user_id = usuario.id)

        #se ele já ta na lista deleta:
        if fav:
            fav.delete()## deleta no banco de Dados
            return redirect('verifica_favoritos')

    else:
        return redirect('login')
