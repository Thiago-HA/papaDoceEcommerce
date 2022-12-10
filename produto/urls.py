from django.urls import path
from . import views


urlpatterns = [
    path('carrinho_add/<int:id>', views.carrinho_add, name='carrinho_add'),
    path('carrinho_remove/<int:id>', views.carrinho_remove, name='carrinho_remove'),
    path('carrinho_remove/endereco/<int:id>', views.carrinho_remove_endereco, name='carrinho_remove_endereco'),
    path('meu_carrinho/', views.carrinho, name='carrinho'),
    path('verifica_carrinho/', views.verifica_carrinho, name='verifica_carrinho'),
    path('endereco_add_carrinho/', views.endereco_add_carrinho, name='endereco_add_carrinho'),
    path('endereco_entrega/', views.endereco_entrega, name='endereco_entrega'),
    path('pagamento/', views.pagamento, name='pagamento'),
]