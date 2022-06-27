from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MaestroUsuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=20)
    tipousu = models.CharField(max_length=50)
    nomusu = models.CharField(max_length=100)
    apeusu = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    dirusu = models.CharField(max_length=300)
    pwd = models.CharField(max_length=50)
    
    def __str__(self):
        return self.rut

class MaestroProducto(models.Model):
    idp = models.IntegerField(primary_key=True)
    nomprod = models.CharField(max_length=100)
    descprod = models.CharField(max_length=300)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="images/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Imagen")
    
    def __str__(self):
        return self.idp

class WebFactura(models.Model):
    nrofac = models.IntegerField(primary_key=True)
    rutcli = models.ForeignKey(MaestroUsuario, models.DO_NOTHING, db_column='rutcli')
    idp = models.ForeignKey(MaestroProducto, models.DO_NOTHING, db_column='idp')
    descfac = models.CharField(max_length=300)
    monto = models.IntegerField()
    
    def __str__(self):
        return self.nrofac

class WebSolicitudServicio(models.Model):
    nross = models.IntegerField(primary_key=True)
    nrofac = models.ForeignKey(WebFactura, models.DO_NOTHING, db_column='nrofac')
    tiposs = models.CharField(max_length=50)

    ruttec = models.ForeignKey(MaestroUsuario, models.DO_NOTHING, db_column='ruttec')
    descss = models.CharField(max_length=200)
    estadoss = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nross

class BodegaGuiaDespacho(models.Model):
    nrogd = models.IntegerField(primary_key=True)
    nrofac = models.ForeignKey('WebFactura', models.DO_NOTHING, db_column='nrofac')
    idp = models.ForeignKey('MaestroProducto', models.DO_NOTHING, db_column='idp')
    estadogd = models.CharField(max_length=50)

    def __str__(self):
        return self.nrogd

class BodegaStockProducto(models.Model):
    idb = models.IntegerField(primary_key=True)
    idp = models.ForeignKey('MaestroProducto', models.DO_NOTHING, db_column='idp')
    nrofac = models.ForeignKey('WebFactura', models.DO_NOTHING, db_column='nrofac', blank=True, null=True)


    def __str__(self):
        return self.idb

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=80, blank=True, null=True, verbose_name="Rut")
    direccion = models.CharField(max_length=80, blank=True, null=True, verbose_name="Direccion")

    def __str__(self):
        return f"{self.user.username} - {self.user.first_name} - {self.user.last_name} ({self.user.email})"

