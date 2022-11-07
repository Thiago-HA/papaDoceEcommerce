from django.contrib import admin
from usuarios.models import Endereco, Usuario, Usuario_endereco

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('nome', 'apelido', 'email', 'senha', 'cpf', 'data_nascimento')

admin.site.register(Endereco)
admin.site.register(Usuario_endereco)