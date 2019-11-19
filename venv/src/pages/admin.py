from django.contrib import admin
from .models import Empresa,Parada,Ruta,Log,Evaluacion

# Register your models here.

admin.site.register(Empresa)
admin.site.register(Parada)
admin.site.register(Ruta)
admin.site.register(Log)
admin.site.register(Evaluacion)