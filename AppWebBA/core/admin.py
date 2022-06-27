from django.contrib import admin
from .models import MaestroUsuario, MaestroProducto,WebSolicitudServicio

# Register your models here.
admin.site.register(MaestroUsuario)
admin.site.register(MaestroProducto)
admin.site.register(WebSolicitudServicio)