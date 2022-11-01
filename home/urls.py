from django.urls import path
from . import views


urlpatterns = [
    path('', views.pagina_home, name='home'),
    path('ver_produto/<int:id>', views.ver_produto, name='ver_produto'),
    path('filtrar/', views.filtrar, name='filtrar'),
    path('favoritos_add/<int:id>', views.favoritos_add, name='favoritos_add'),
    path('favoritos_remove/<int:id>', views.favoritos_remove, name='favoritos_remove'),
]