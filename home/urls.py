from django.urls import path
from . import views


urlpatterns = [
    path('', views.pagina_home, name='home'),
    path('ver_produto/<int:id>', views.ver_produto, name='ver_produto'),
    path('filtrar/', views.filtrar, name='filtrar'),
]