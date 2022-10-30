from django.shortcuts import HttpResponse, redirect, render
from usuarios.models import Usuario
from produto.models import Produto, Categoria

# Create your views here.
def pagina_home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        produtos = Produto.objects.all() ## mostra todos os produtos.
        categorias = Categoria.objects.all()

        context = {
            'categorias': categorias,
            'produtos': produtos,
        }

        return render(request, 'home_autenticado.html', context)
    else:
        produto = Produto.objects.all() ## mostra todos os produtos.
        return render(request, 'home.html', {'produtos': produto})

def ver_produto(request, id):
    if request.session.get('usuario'):
        produto = Produto.objects.get(id = id)
        return render(request, 'ver_produto_autenticado.html', {'produto' : produto})
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