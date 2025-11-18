from django.contrib import admin
from .models import Producto, Pedido, Cliente, PerfilCliente

admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Cliente)
admin.site.register(PerfilCliente)

