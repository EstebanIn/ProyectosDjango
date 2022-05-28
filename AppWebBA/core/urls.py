from django.urls import path
from .views import index, InicioSesion, RegistroCliente, FichaProducto, Facturas, ConsultaSolicitudServicio

urlpatterns = [
    path('', index, name="index"),
    path('InicioSesion/', InicioSesion, name="InicioSesion"),
    path('RegistroCliente/', RegistroCliente, name="RegistroCliente"),
    path('FichaProducto/<action>/<id>', FichaProducto, name="FichaProducto"),
    path('Facturas/<id>', Facturas, name="Facturas"),
    path('ConsultaSolicitudServicio/', ConsultaSolicitudServicio, name="ConsultaSolicitudServicio"),
    
]