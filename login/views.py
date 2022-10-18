import email
from django.shortcuts import HttpResponse, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()
        mail = User.objects.filter(email=email).first()

        if user or mail:
            return HttpResponse('Usurio ou email já existe no banco de dados')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return HttpResponse(username)

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user is not None:
            login_django(request, user)
            return HttpResponse('autenticado')
        else: 
            return HttpResponse('email ou senha inválidos')

def perfil(request):
    if request.user.is_authenticated:
        return HttpResponse('perfil')
    else:
        return render(request, 'login.html')


