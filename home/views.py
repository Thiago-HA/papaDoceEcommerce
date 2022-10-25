from multiprocessing import context
from django.shortcuts import redirect, render
from usuarios.models import Usuario
from produto.models import Produto

# Create your views here.
def pagina_home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        produtos = Produto.objects.all() ## mostra todos os produtos.
        return render(request, 'home_autenticado.html', {'produtos': produtos})
    else:
        
        produtos = Produto.objects.all() ## mostra todos os produtos.
        return render(request, 'home.html', {'produtos': produtos})
        

    
