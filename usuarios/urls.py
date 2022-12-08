

from django.urls import path
from . import views


urlpatterns = [
    path('login/',  views.login, name='login'),
    path('cadastro/',  views.cadastro, name='cadastro'),
    path('valida_cadastro/',  views.valida_cadastro, name='valida_cadastro'),
    path('valida_login/',  views.valida_login, name='valida_login'),
    path('sair/', views.sair, name='sair'),
    path('minha_conta/perfil/', views.perfil, name='perfil'),
    path('minha_conta/perfil/update_perfil/', views.update_perfil, name='update_perfil'),
    path('minha_conta/perfil/update_endereco/<int:id>', views.update_endereco, name='update_endereco'),
    path('minha_conta/perfil/endereco_add/', views.endereco_add, name='endereco_add'),
    path('minha_conta/perfil/endereco_remove/<int:id>', views.endereco_remove, name='endereco_remove'),
]


