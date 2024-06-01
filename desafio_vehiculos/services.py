from .models import Vehiculo, Chofer, RegistroContabilidad
from datetime import datetime

#Crea vehiculo
def crear_vehiculo(patente, marca, modelo, year, activo):
    vehiculo = Vehiculo(
        patente=patente, 
        marca=marca, 
        modelo=modelo, 
        year=year, 
        activo=activo
        )
    vehiculo.save()
    return vehiculo

#Crea chofer y asocia a un vehiculo
def crear_chofer(rut, nombre, apellido, activo, vehiculo_id):
    vehiculo = obtener_vehiculo(vehiculo_id)
    chofer = Chofer(
        rut=rut, 
        nombre=nombre, 
        apellido=apellido,
        activo=activo,
        vehiculo_id=vehiculo
        )
    chofer.save()
    return chofer

def crear_registro_contable(fecha_compra, valor, vehiculo_id):
    try:
        vehiculo = Vehiculo.objects.get(patente=vehiculo_id)
        registro = RegistroContabilidad.objects.create(
            fecha_compra=fecha_compra, 
            valor=valor,
            vehiculo=vehiculo  # Referencia correcta al campo de relación
        )
        return registro
    except Vehiculo.DoesNotExist:
        print(f"No se encontró un vehículo con la patente {vehiculo_id}")
        return None

def deshabilitar_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    chofer.activo = False
    chofer.save()
    return chofer

def deshabilitar_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    vehiculo.activo = False
    vehiculo.save()
    return vehiculo

def habilitar_chofer(rut):
    try:
        chofer = Chofer.objects.get(rut=rut)
        chofer.activo = True
        chofer.save()
        return chofer
    except Vehiculo.DoesNotExist:
        print(f"No se encontró un chofer con el rut {rut}")
        return None

def habilitar_vehiculo(patente):
    try:
        vehiculo = Vehiculo.objects.get(patente=patente)
        vehiculo.activo = True
        vehiculo.save()
        return vehiculo
    except Vehiculo.DoesNotExist:
        print(f"No se encontró un vehículo con la patente {patente}")
        return None

def obtener_vehiculo(patente):
    return Vehiculo.objects.get(patente=patente)

def obtener_chofer(rut):
    return Chofer.objects.get(rut=rut)



# def asignar_chofer_a_vehiculo(rut, patente):
#     chofer = Chofer.objects.get(rut=rut)
#     vehiculo = Vehiculo.objects.get(patente=patente)
#     chofer.vehiculo = vehiculo
#     chofer.save()
#     return chofer

def imprimir_datos_vehiculos():
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        print(f"Patente: {vehiculo.patente}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.year}")
