from django.db import models

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



class Parada(models.Model):
    """
    Paradas de una ruta
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    nombre = models.CharField(max_length=10000, unique=True)
    description = models.CharField(max_length=10000)
    horario = models.CharField(max_length=10000)
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __str__(self):
        return f'c/{self.nombre}'
    

class Ruta(models.Model):
    """
    Ruta de una Empresa
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=10000, unique=True)
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

