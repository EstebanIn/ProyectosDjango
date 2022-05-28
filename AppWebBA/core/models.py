from django.db import models

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
    
    def __str__(self):
        return self.idp

class WebFactura(models.Model):
    nrofac = models.IntegerField(primary_key=True)
    rutcli = models.ForeignKey(MaestroUsuario, models.DO_NOTHING, db_column='rutcli')
    idp = models.ForeignKey(MaestroProducto, models.DO_NOTHING, db_column='idp')
    fechafac = models.DateField()
    descfac = models.CharField(max_length=300)
    monto = models.IntegerField()
    
    def __str__(self):
        return self.nrofac

class WebSolicitudServicio(models.Model):
    nross = models.IntegerField(primary_key=True)
    nrofac = models.ForeignKey(WebFactura, models.DO_NOTHING, db_column='nrofac')
    tiposs = models.CharField(max_length=50)
    fechavisita = models.DateField()
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

