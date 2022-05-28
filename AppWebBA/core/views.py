from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def InicioSesion(request):
    return render(request, 'core/InicioSesion.html')

def RegistroCliente(request):
    return render(request, 'core/RegistroCliente.html')

def FichaProducto(request):
    return render(request, 'core/FichaProducto.html')

def Facturas(request):
    return render(request, 'core/Facturas.html')

def ConsultaSolicitudServicio(request):
    return render(request, 'core/ConsultaSolicitudServicio.html')