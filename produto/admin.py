from django.contrib import admin
from .models import Produto, Categoria, Carrinho

# Register your models here.
admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Carrinho)