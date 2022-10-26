from multiprocessing import context
from django.shortcuts import HttpResponse, redirect, render
from usuarios.models import Usuario
from produto.models import Produto

# Create your views here.
def pagina_home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        produtos = Produto.objects.all() ## mostra todos os produtos.
        return render(request, 'home_autenticado.html', {'produtos': produtos})
    else:
        produto = Produto.objects.all() ## mostra todos os produtos.
        return render(request, 'home.html', {'produtos': produto})

def ver_produto(request, id):
    if request.session.get('usuario'):
        produto = Produto.objects.get(id = id)
        return render(request, 'ver_produto_autenticado.html', {'produto' : produto})
    else:
        return render(request,'ver_produto.html')

    
