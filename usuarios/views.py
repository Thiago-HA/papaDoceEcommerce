import email
import re
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Usuario
from hashlib import sha256 ## 

def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

def valida_cadastro(request):

    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    email = request.POST.get('email')

    usuario = Usuario.objects.filter(email = email)

    ## SE nome ou email for igual a zero 
    if len(nome.strip()) == 0 or len(email.strip()) == 0: ##len() se refere ao tamanho e .strip() retira os espaços do inicio e do final.
        return redirect('/auth/cadastro/?status=1')

    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')

    if(len(usuario)): ## Se o tamanho do usuario for maior que 0:
        return redirect('/auth/cadastro/?status=3')
    
    try:
        senha = sha256(senha.encode()).hexdigest() ##sha256 cria um hash de senha e o Hexdigest() faz a conversão do hash
                                                    ## para um conjunto em hexadecimal de 64 caracteries
        usuario = Usuario(nome = nome, senha = senha, email = email)
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



    

