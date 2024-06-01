from django.db import models

class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True)
    marca = models.CharField(max_length=20, null =False, blank = False)
    modelo = models.CharField(max_length=20, null =False, blank = False)
    year = models.IntegerField(null =False, blank = False)
    activo = models.BooleanField(default =True)
    creacion_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.patente} - {self.marca} {self.modelo} ({self.year}) - {self.activo}"

class Chofer(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null =False, blank = False)
    apellido = models.CharField(max_length=50, null =False, blank = False)
    activo = models.BooleanField(default=False)
    vehiculo_id = models.OneToOneField('Vehiculo', related_name='chofer', on_delete=models.PROTECT, unique=True)
    creacion_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rut}) - {self.activo}"

class RegistroContabilidad(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_compra = models.DateField(null =False, blank = False)
    valor = models.FloatField(null =False, blank = False)
    vehiculo = models.OneToOneField('Vehiculo', related_name='registrocontable', on_delete=models.PROTECT, unique=True)
    creacion_registro = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Registro {self.id} - Vehículo: {self.vehiculo.patente}"
