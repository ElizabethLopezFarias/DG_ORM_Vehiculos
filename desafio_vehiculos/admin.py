from django.contrib import admin

# Register your models here.
from .models import Vehiculo, Chofer, RegistroContabilidad

admin.site.register(Vehiculo)
admin.site.register(Chofer)
admin.site.register(RegistroContabilidad)