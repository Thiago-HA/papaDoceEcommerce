from django.shortcuts import render


# Create your views here.
def pagina_home(request):

    context = {

        'produtos':[
            {'nome': 'Carregador de celular', 'preco': '40,00'},
            {'nome': 'Capinha de Celular ', 'preco': '50,00'},
            {'nome': 'Fone de Ouvido ', 'preco': '32,00'},
            {'nome': 'PowerBank ', 'preco': '84,50'},
            {'nome': 'Fone de Ouvido ', 'preco': '32,00'},
            {'nome': 'PowerBank ', 'preco': '84,50'},
            {'nome': 'Capinha de Celular ', 'preco': '50,00'},
            {'nome': 'Fone de Ouvido ', 'preco': '32,00'},
            {'nome': 'PowerBank ', 'preco': '84,50'},
            {'nome': 'Fone de Ouvido ', 'preco': '32,00'},
            {'nome': 'PowerBank ', 'preco': '84,50'},
            {'nome': 'PowerBank ', 'preco': '84,50'},
            {'nome': 'Fone de Ouvido ', 'preco': '32,00'},
            {'nome': 'PowerBank ', 'preco': '84,50'},
            {'nome': 'Capinha de Celular ', 'preco': '50,00'},
            {'nome': 'Fone de Ouvido ', 'preco': '32,00'},
            {'nome': 'PowerBank ', 'preco': '84,50'},
            {'nome': 'Fone de Ouvido ', 'preco': '32,00'},
            {'nome': 'PowerBank ', 'preco': '84,50'},
        ], 
        
        'filtros':[
            {'descricao': 'Confeitaria'},
            {'descricao': 'artigos de festas'},
            {'descricao': 'Balão'},
            {'descricao': 'Outros'},
        ]
        
    }


    return render(request, 'home.html', context)