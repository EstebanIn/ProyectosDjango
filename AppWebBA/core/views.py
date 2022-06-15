from django.shortcuts import redirect , render
from django. contrib.auth import login, logout, authenticate
from django. contrib.auth.forms import UsernameField
from django. contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
## importar modelos y formularios
from .models import MaestroProducto, MaestroUsuario, PerfilUsuario
from .forms import IniciarSesionForm, MaestroProductoForm, RegistrarUsuarioForm, PerfilUsuarioForm
## importar la libreria de webpay
##from transbank.webpay.webpay_plus.transaction import Transaction, WebpayOptions
import random


## VISTAS RELACIONADAS CON LA WEBPAY
#https://www.transbankdevelopers.cl/documentacion/como_empezar#como-empezar
#https://www.transbankdevelopers.cl/documentacion/como_empezar#codigos-de-comercio
#https://www.transbankdevelopers.cl/referencia/webpay

# Tipo de tarjeta   Detalle                        Resultado
#----------------   -----------------------------  ------------------------------
# VISA              4051885600446623
#                   CVV 123
#                   cualquier fecha de expiración  Genera transacciones aprobadas.
# AMEX              3700 0000 0002 032
#                   CVV 1234
#                   cualquier fecha de expiración  Genera transacciones aprobadas.
# MASTERCARD        5186 0595 5959 0568
#                   CVV 123
#                   cualquier fecha de expiración  Genera transacciones rechazadas.
# Redcompra         4051 8842 3993 7763            Genera transacciones aprobadas (para operaciones que permiten débito Redcompra y prepago)
# Redcompra         4511 3466 6003 7060            Genera transacciones aprobadas (para operaciones que permiten débito Redcompra y prepago)
# Redcompra         5186 0085 4123 3829            Genera transacciones rechazadas (para operaciones que permiten débito Redcompra y prepago)
"""

@csrf_exempt
def iniciar_pago(request):
    print("Webpay Plus Transaction.create")
    buy_order = str(random.randrange(1000000, 99999999))
    session_id = request.user.username
    amount = random.randrange(10000, 1000000)
    return_url = 'http://127.0.0.1:8000/pago_exitoso/'

    # response = Transaction.create(buy_order, session_id, amount, return_url)
    commercecode = "597055555532"
    apikey = "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C"

    tx = Transaction(options=WebpayOptions(commerce_code=commercecode, api_key=apikey, integration_type="TEST"))
    response = tx.create(buy_order, session_id, amount, return_url)
    print(response['token'])

    perfil = PerfilUsuario.objects.get(user=request.user)
    form = PerfilUsuarioForm()

    context = {
        "buy_order": buy_order,
        "session_id": session_id,
        "amount": amount,
        "return_url": return_url,
        "response": response,
        "token_ws": response['token'],
        "url_tbk": response['url'],
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "email": request.user.email,
        "rut": perfil.rut,
        "direccion": perfil.direccion,
    }

    return render(request, "core/iniciar_pago.html", context)

@csrf_exempt
def pago_exitoso(request):

    if request.method == "GET":
        token = request.GET.get("token_ws")
        print("commit for token_ws: {}".format(token))
        commercecode = "597055555532"
        apikey = "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C"
        tx = Transaction(options=WebpayOptions(commerce_code=commercecode, api_key=apikey, integration_type="TEST"))
        response = tx.commit(token=token)
        print("response: {}".format(response))

        user = User.objects.get(username=response['session_id'])
        perfil = PerfilUsuario.objects.get(user=user)
        form = PerfilUsuarioForm()

        context = {
            "buy_order": response['buy_order'],
            "session_id": response['session_id'],
            "amount": response['amount'],
            "response": response,
            "token_ws": token,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "rut": perfil.rut,
            "direccion": perfil.direccion,
            "response_code": response['response_code']
        }

        return render(request, "core/pago_exitoso.html", context)
    else:
        return redirect(home)

"""

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def index(request):
    return render(request, 'core/index.html')


## vistas crud de sesion
def InicioSesion(request):
    data = {"mesg": "", "form": IniciarSesionForm()}

    if request.method == "POST":
        form = IniciarSesionForm(request.POST)
        if form.is_valid:
            username = request.POST.GET("username")
            password = request.POST.GET("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(home)
                else:
                    data['mesg'] = '!La contraseña o el usuario no es correcto¡'
            else:
                data['mesg'] = '!La contraseña o el usuario no es correcto¡'
    return render(request, 'core/InicioSesion.html', data)

def CerrarSesion(request):
    logout(request)
    return redirect(home)

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            rut = request.POST.get("rut")
            direccion = request.POST.get("direccion")
            PerfilUsuario.objects.update_or_create(user=user, rut=rut, direccion=direccion)
            return redirect(InicioSesion)
    form = RegistrarUsuarioForm()
    return render(request, "core/registrar_usuario.html", context={'form': form})

def Perfil_Usuario(request):
    data = {"mesg": "", "form": PerfilUsuarioForm}

    if request.method == 'POST':
        form = PerfilUsuarioForm(request.POST)
        if form.is_valid():
            user = request.user
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.email = request.POST.get("email")
            user.save()
            perfil = PerfilUsuario.objects.get(user=user)
            perfil.rut = request.POST.get("rut")
            perfil.direccion = request.POST.get("direccion")
            perfil.save()
            data["mesg"] = "¡Sus datos fueron actualizados correctamente!"

    perfil = PerfilUsuario.objects.get(user=request.user)
    form = PerfilUsuarioForm()
    form.fields['first_name'].initial = request.user.first_name
    form.fields['last_name'].initial = request.user.last_name
    form.fields['email'].initial = request.user.email
    form.fields['rut'].initial = perfil.rut
    form.fields['direccion'].initial = perfil.direccion
    data["form"] = form
    return render(request, "core/perfil_usuario.html", data)



## catagolo
def tienda(request):
    data = {'list': MaestroProducto.objects.all().order_by('idp')}
    return render(request, 'core/tienda.html', data)




### vistas de los productos
def AdministrarProducto(request, action, id):
    if not (request.user.is_authenticated and request.user.is_staff):
        return redirect(home)

    data = {"mesg": "", "form": MaestroProductoForm, "action": action, "id": id, "formsesion": IniciarSesionForm}

    if action == 'ins':
        if request.method == 'POST':
            form = MaestroProducto(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data['mesg'] = "!El producto fue creado correctamente¡"
                except:
                    data['mesg'] = "!No se puede crear dos productos con el mismo identificador¡"
    
    elif action == 'upd':
        objeto = MaestroProducto.objects.get(idp=id)
        if request.method == "POST":
            form = MaestroProductoForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El vehículo fue actualizado correctamente!"
        data["form"] = MaestroProductoForm(instance=objeto)

    elif action == 'del':
        try:
            MaestroProducto.objects.get(idp=id).delete()
            data["mesg"] = "¡El vehículo fue eliminado correctamente!"
            return redirect(AdministrarProducto, action='ins', id = '-1')
        except:
            data["mesg"] = "¡El vehículo ya estaba eliminado!"

    data["list"] = MaestroProducto.objects.all().order_by('idp')
    return render(request, "core/administrar_productos.html", data)

def Facturas(request):
    return render(request, 'core/Facturas.html')

def ConsultaSolicitudServicio(request):
    return render(request, 'core/ConsultaSolicitudServicio.html')