from django.urls import path
from . import views


urlpatterns = [
    path('verifica_pagamento/',  views.verifica_pagamento, name='verifica_pagamento'),
    path('meus_pedidos/',  views.meus_pedidos, name='pedidos'),
    path('verifica_meus_pedidos/',  views.verifica_meus_pedidos, name='verifica_meus_pedidos'),


]
 