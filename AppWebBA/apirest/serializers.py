from rest_framework import serializers
from core.models import MaestroProducto

class MaestroProductoSerializers(serializers.ModelSerializer):
        class Meta:
            model = MaestroProducto
            fields = ['rut', 'tipousu', 'nomusu', 'apeusu', 'correo', 'dirusu', 'pwd']