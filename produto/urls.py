from django.urls import path
from . import views


urlpatterns = [
    path('carrinho_add/<int:id>', views.carrinho_add, name='carrinho_add'),
    path('carrinho_remove/<int:id>', views.carrinho_remove, name='carrinho_remove'),
    path('meu_carrinho/', views.carrinho, name='carrinho'),
    path('verifica_carrinho/', views.verifica_carrinho, name='verifica_carrinho'),
]