from django.shortcuts import redirect, render
from produto.models import Produto
from .models import Endereco, Usuario, Usuario_endereco
from hashlib import sha256 ## 

def login(request):
    if request.session.get('usuario'):
        return redirect('/')
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def cadastro(request):
    if request.session.get('usuario'):
        return redirect('/')
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

def valida_cadastro(request):

    nome = request.POST.get('nome')
    apelido = request.POST.get('apelido')
    senha = request.POST.get('senha')
    email = request.POST.get('email')
    cpf = request.POST.get('cpf')
    data_nascimento = request.POST.get('data_nascimento')

    usuario_email = Usuario.objects.filter(email = email)
    usuario_cpf = Usuario.objects.filter(cpf = cpf)

    ## SE nome ou email for igual a zero 
    if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(cpf.strip()) == 0 or len(data_nascimento.strip()) == 0: 
        ##len() se refere ao tamanho e .strip() retira os espaços do inicio e do final.
        return redirect('/auth/cadastro/?status=1')

    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')

    if(len(usuario_email)): ## Se o tamanho do usuario for maior que 0:
        return redirect('/auth/cadastro/?status=3')

    if(len(usuario_cpf)): ## Se o tamanho do usuario for maior que 0:
        return redirect('/auth/cadastro/?status=5')
    
    try:
        senha = sha256(senha.encode()).hexdigest() ##sha256 cria um hash de senha e o Hexdigest() faz a conversão do hash
                                                    ## para um conjunto em hexadecimal de 64 caracteries
        usuario = Usuario(nome = nome, senha = senha, email = email, apelido = apelido, cpf = cpf, data_nascimento = data_nascimento)
        usuario.save()## salva no banco de Dados

        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')


def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email = email).filter(senha = senha)

    ## SE email ou senha for igual a zero 
    if len(email.strip()) == 0 or len(senha.strip()) == 0: ##len() se refere ao tamanho e .strip() retira os espaços do inicio e do final.
        return redirect('/auth/login/?status=1')
    elif(len(usuario) == 0):
        return redirect('/auth/login/?status=1')## se não existir o usuario no sistema redireciona para login com status 1
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id ##session funciona como se fosse uma variavel global para autenticar o usuario.
        return redirect('home')


def sair(request):
    ## request.session = None
    request.session.flush() ## .flush() garante que a session esteja completamente vazia! 
    return redirect('/auth/login')


def perfil(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        usuariostr = str(usuario.id)
        #lista de todos os endereços deste usuario:
        #enderecos = Endereco.objects.raw('SELECT * FROM (usuarios_endereco INNER JOIN usuarios_usuario_endereco ON usuarios_endereco.id = usuarios_usuario_endereco.endereco_id) INNER JOIN usuarios_usuario ON usuarios_usuario_endereco.user_id = usuarios_usuario.id WHERE  usuarios_usuario_endereco.user_id = %s;', [usuariostr])
        enderecos = Usuario_endereco.objects.filter(user = usuario.id)

        #carregar a quantidade na lista de favoritos:
        fav = Produto.objects.raw('SELECT * FROM (produto_produto INNER JOIN produto_favorito ON produto_produto.id = produto_favorito.prod_id) INNER JOIN usuarios_usuario ON produto_favorito.user_id = usuarios_usuario.id WHERE  produto_favorito.user_id = %s;', [usuariostr])
        qtd_favoritos = len(fav)

        #carregar a quantidade na lista de Carrinho:
        carrinho = Produto.objects.raw('SELECT * FROM (produto_produto INNER JOIN produto_carrinho ON produto_produto.id = produto_carrinho.produto_id) INNER JOIN usuarios_usuario ON produto_carrinho.user_id = usuarios_usuario.id WHERE  produto_carrinho.user_id = %s;', [usuariostr])
        qtd_carrinho = len(carrinho)

        status = request.GET.get('status')

        context = {
            'usuario' : usuario,
            'endereco' : enderecos,
            'qtd_favoritos' : qtd_favoritos,
            'qtd_carrinho' : qtd_carrinho,
            'status' : status,
        }

        return render(request, 'perfil.html', context)    


    else:
        return redirect('login')

def update_perfil(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        usuariostr = str(usuario.id)
        nome = request.POST.get('nome')
        apelido = request.POST.get('apelido')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        data_nascimento = request.POST.get('data_nascimento')
        
        usuario_email = Usuario.objects.filter(email = email)
        usuario_cpf = Usuario.objects.filter(cpf = cpf)

         ## SE nome ou email for igual a zero 
        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(cpf.strip()) == 0 or len(data_nascimento.strip()) == 0: 
            ##len() se refere ao tamanho e .strip() retira os espaços do inicio e do final.
            return redirect('/auth/minha_conta/perfil/?status=2')

        if(len(usuario_email) and email != str(usuario.email)): ## Se o tamanho do usuario for maior que 0:
            return redirect('/auth/minha_conta/perfil/?status=3')

        if(len(usuario_cpf) and cpf != str(usuario.cpf)): ## Se o tamanho do usuario for maior que 0:
            return redirect('/auth/minha_conta/perfil/?status=4')

        try:
            user = Usuario(id = usuario.id, nome = nome, senha = usuario.senha, email = email, apelido = apelido, cpf = cpf, data_nascimento = data_nascimento)
            user.save()

            return redirect('/auth/minha_conta/perfil/?status=1')
        except:
            return redirect('/auth/minha_conta/perfil/?status=5')

    else:
        return redirect('login')

    
def update_endereco(request, id):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        cep = request.POST.get('cep')
        complemento = request.POST.get('complemento')
        
        

         ## SE os campos obrigatórios for igual a zero 
        if len(rua.strip()) == 0 or len(numero.strip()) == 0 or len(bairro.strip()) == 0 or len(cidade.strip()) == 0 or len(cep.strip()) == 0: 
            ##len() se refere ao tamanho e .strip() retira os espaços do inicio e do final.
            return redirect('/auth/minha_conta/perfil/?status=2')

        try:
            endereco = Endereco(id = id,  rua = rua, numero = numero, bairro = bairro, cidade= cidade, cep = cep, complemento = complemento)
            endereco.save()

            return redirect('/auth/minha_conta/perfil/?status=1')
        except:
            return redirect('/auth/minha_conta/perfil/?status=5')

    else:
        return redirect('login')

def endereco_add(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        cep = request.POST.get('cep')
        complemento = request.POST.get('complemento')
        
        

         ## SE os campos obrigatórios for igual a zero 
        if len(rua.strip()) == 0 or len(numero.strip()) == 0 or len(bairro.strip()) == 0 or len(cidade.strip()) == 0 or len(cep.strip()) == 0: 
            ##len() se refere ao tamanho e .strip() retira os espaços do inicio e do final.
            return redirect('/auth/minha_conta/perfil/?status=2')

        try:
            endereco = Endereco(rua = rua, numero = numero, bairro = bairro, cidade= cidade, cep = cep, complemento = complemento)
            endereco.save()

            usuario_endereco = Usuario_endereco(user_id = usuario.id, endereco_id = endereco.id)
            usuario_endereco.save()

            return redirect('/auth/minha_conta/perfil/?status=1')
        except:
            return redirect('/auth/minha_conta/perfil/?status=5')

    else:
        return redirect('login')

def endereco_remove(request, id):
    if request.session.get('usuario'):
        
        endereco = Endereco.objects.get(id = id)

        endereco.delete()## deleta no banco de Dados
        return redirect('/auth/minha_conta/perfil/?status=6')


    else:
        return redirect('login')
