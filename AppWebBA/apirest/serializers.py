from rest_framework import serializers
from core.models import MaestroUsuario, MaestroProducto

class MaestroUsuarioSerializers(serializers.ModelSerializer):
        class Meta:
            model = MaestroUsuario
            fields = ['rut', 'tipousu', 'nomusu', 'apeusu', 'correo', 'dirusu', 'pwd']

class MaestroProductoSerializers(serializers.ModelSerializer):
        class Meta:
            model = MaestroProducto
            fields = ['idp', 'nomprod', 'descprod', 'precio']