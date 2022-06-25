from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

from .views import Perfil_Usuario, index, home, AdministrarProducto

from .views import InicioSesion, RegistroCliente, CerrarSesion

from .views import Facturas, ConsultaSolicitudServicio, Tienda 

from .poblarbd import poblarbd

urlpatterns = [
    path('', home, name="home"),
    path('InicioSesion/', InicioSesion, name="InicioSesion"),
    path('poblarbd', poblarbd, name="poblarbd"),
    path('cerrar_sesion/', CerrarSesion, name='cerrar_sesion'),
    path('RegistroCliente/', RegistroCliente, name="RegistroCliente"),
    path('Facturas/<id>', Facturas, name="Facturas"),
    path('ConsultaSolicitudServicio/', ConsultaSolicitudServicio, name="ConsultaSolicitudServicio"),

    path('index', index, name="index"),
   ## path('poblar_bd', poblar_bd, name="poblar_bd"),
    
    path('administrar_productos/<action>/<id>', AdministrarProducto, name="administrar_productos"),


    path('password_cambiada/', TemplateView.as_view(template_name='core/password_cambiada.html'), name='password_cambiada'),
    path('cambiar_password/', auth_views.PasswordChangeView.as_view(template_name='core/cambiar_password.html', success_url='/password_cambiada'), name='cambiar_password'),


    path('tienda/<id>', Tienda, name="tienda"),

    path('perfil_usuario/', Perfil_Usuario, name="perfil_usuario"),
   
]