from django import forms
from django.froms import ModelForm, fields
from .models import MaestroProducto, MaestroUsuario, WebFactura, WebSolicitudServicio, BodegaGuiaDespacho, BodegaStockProducto


class MaestroProductoForm(ModelForm):
        class Meta:
            models MaestroProducto
            fields = ["rut", "tipousu", "nomusu", "apeusu", "correo", "dirusu", "pwd"]