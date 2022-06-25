from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import *
from .views import AdministrarProducto
def poblarbd(request):
    try:
        print("Verificar si existe usuario cliente.")
        if User.objects.filter(username="usuario_cliente").exists():
            print("Intentando eliminar usuario cliente.")
            User.objects.get(username="usuario_cliente").delete()
            print("Usuario cliente eliminado.")
        print("Iniciando creación de usuario cliente.")
        user = User.objects.create_user(username="usuario_cliente", password='Duoc@123')
        user.first_name = "Chris"
        user.last_name = "Evans (Cliente)"
        user.email = "cevans@marvel.com"
        user.is_superuser = False
        user.is_staff = False
        PerfilUsuario.objects.create(user=user, rut="11.111.111-K", direccion="Burbank (Estados Unidos)")
        user.save()
        print("Usuario cliente fue creado correctamente.")
    except Exception as err:
        print(f"Error al crear usuario cliente: {err}")
    try:
        print("Verificar si existe usuario staff.")
        if User.objects.filter(username="usuario_staff").exists():
            print("Intentando eliminar usuario staff.")
            User.objects.get(username="usuario_staff").delete()
            print("Usuario staff eliminado.")
        print("Iniciando creación de usuario staff.")
        user = User.objects.create_user(username="usuario_staff", password='Duoc@123')
        user.first_name = "Pepper"
        user.last_name = "Potts (Staff)"
        user.email = "ppotts@tiendastark.com"
        user.is_superuser = True
        user.is_staff = True
        PerfilUsuario.objects.create(user=user, rut="22.222.222-K", direccion="Burbank (Estados Unidos)")
        user.save()
        print("Usuario staff fue creado correctamente.")
    except Exception as err:
        print(f"Error al crear usuario staff: {err}")
    try:
        MaestroProducto.objects.all().delete()
        print("Tabla Vehiculo fue truncada.")
    except Exception as err:
        print(f"Error al poblar tabla Categoria: {err}")
    try:
        print("Iniciar poblamiento de tabla Vehiculo.")
        MaestroProducto.objects.create(idp="1,", nomprod='Aire Wifi 9000 btu', modelo="Enfría 9-16 m2", precio=299990),
        MaestroProducto.objects.create(idp="2,", nomprod='Split Inv 12000 btu', modelo="Frío/Calor AR12", precio=450000),
        MaestroProducto.objects.create(idp="3,", nomprod='Anwo VP', modelo="9000 Virus Protect", precio=288990),
        MaestroProducto.objects.create(idp="4,", nomprod='Anwo Portátil-Benz', modelo="12000 btu", precio=131990),
        MaestroProducto.objects.create(idp="5,", nomprod='GPORT-14', modelo="Anwo 14000 btu", precio=399990),
        MaestroProducto.objects.create(idp="6", nomprod='Kendal', modelo="Climat 22-24 m2", precio=335990),
        print("Tabla Vehiculo fue poblada.")
    except Exception as err:
        print(f"Error al poblar vehículos: {err}")
    return redirect(AdministrarProducto, action='ins', id = '-1')