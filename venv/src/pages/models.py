from django.db import models
from django.contrib.auth.models import User


class Empresa(models.Model):
    """
    Empresas que tienen rutas
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    nombre = models.CharField(max_length=10000, unique=True)
    description = models.CharField(max_length=10000)
    direccion = models.CharField(max_length=10000)
    horario = models.CharField(max_length=10000)
    telefono = models.CharField(max_length=10000)
    correo = models.EmailField()
    serv_origen = models.CharField(max_length=10000)
    serv_destino = models.CharField(max_length=10000)
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __str__(self):
        return f'{self.nombre}'


class Ruta(models.Model):
    """
    Ruta de una Empresa
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=10000, unique=True)
    nombre_destino = models.CharField(max_length=10000)
    description = models.CharField(max_length=10000)
    costo = models.FloatField()
    horario = models.CharField(max_length=10000)
    duracion_viaje = models.CharField(max_length=10000)
    inclusivo = models.BooleanField(verbose_name='Apto para discapacitados', default=False)

    origen_latitud = models.FloatField()
    origen_longitud = models.FloatField()

    destino_latitud = models.FloatField()
    destino_longitud = models.FloatField()

    def __str__(self):
        return f'c/{self.nombre}'


class Parada(models.Model):
    """
    Paradas de una ruta
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=10000, unique=False)
    description = models.CharField(max_length=10000)
    horario = models.CharField(max_length=10000)
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __str__(self):
        return f'c/{self.nombre}'


class Log(models.Model):
    """
    Bitacora

    <accion> = actualizar | borrar | crear

    operacion=<accion> ruta
    operacion=<accion> empresa
    operacion=<accion> parada

    """
    usuario = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    fecha_creacion = models.DateTimeField(auto_now=True)
    operacion = models.CharField(max_length=10000)
    empresa = models.ForeignKey(Empresa, null=True, on_delete=models.SET_NULL)
    ruta = models.ForeignKey(Ruta, null=True, on_delete=models.SET_NULL)
    parada = models.ForeignKey(Parada, null=True, on_delete=models.SET_NULL)

    def __str__(self):

        return f'{self.operacion} Fecha: {self.fecha_creacion}'

