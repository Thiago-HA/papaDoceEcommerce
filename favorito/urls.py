from django.urls import path
from . import views


urlpatterns = [
    path('favoritos/',  views.favoritos, name='favoritos'),
    path('verifica_favoritos/',  views.verifica_favoritos, name='verifica_favoritos'),
]
 