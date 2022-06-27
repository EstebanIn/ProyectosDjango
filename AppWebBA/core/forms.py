from dataclasses import field
from pyexpat import model
from django import forms
from django.forms import ModelForm, fields, Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import MaestroProducto, MaestroUsuario, PerfilUsuario, WebSolicitudServicio, WebFactura


class MaestroProductoForm(ModelForm):
        class Meta:
            model = MaestroProducto
            fields = ['idp', 'nomprod', 'descprod', 'precio']

class IniciarSesionForm(Form):
    correo = forms.CharField(widget=forms.TextInput(), label="correo")
    pwd = forms.CharField(widget=forms.PasswordInput(), label="pwd")
    class Meta:
        fields = ['correo', 'pwd']

class RegistrarUsuarioForm(UserCreationForm):
    rut = forms.CharField(max_length=80, required=True, label="Rut")
    direccion = forms.CharField(max_length=80, required=True, label="Direccion")
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','rut','direccion']

class PerfilUsuarioForm(Form):
    first_name = forms.CharField(max_length=150, required=True, label="Nombres") 
    last_name = forms.CharField(max_length=150, required=True, label="Apellidos")
    email = forms.CharField(max_length=260, required=True, label="Correo")
    rut = forms.CharField(max_length=80, required=False, label="Rut")
    direccion = forms.CharField(max_length=80, required=False, label="Direccion")

class WebSolicitudServicioForm(ModelForm):
    tiposs = forms.CharField(max_length=50)
    descss = forms.CharField(max_length=200)
    estadoss = forms.CharField(max_length=50)
    class Meta:
        fields = '__all__'


##class WebSolicitudServicioForm(ModelForm):
##    tiposs = forms.CharField(max_length=50)
##    fechavisita = forms.DateField()
##    descss = forms.CharField(max_length=200)
##    estadoss = forms.CharField(max_length=50)
##    class Meta:
##        model = WebSolicitudServicio
##        fields = ['tiposs','fechavisita','tiposs']
