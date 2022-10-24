

from django.urls import path
from . import views


urlpatterns = [
    path('login/',  views.login, name='login'),
    path('cadastro/',  views.cadastro, name='cadastro'),
    path('valida_cadastro/',  views.valida_cadastro, name='valida_cadastro'),
    path('valida_login/',  views.valida_login, name='valida_login'),
    path('valida_user_home/',  views.valida_user_home, name='valida_user_home'),
    path('sair/', views.sair, name='sair'),
]


