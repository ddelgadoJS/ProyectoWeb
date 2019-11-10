from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import *

class EmpresaCreateForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            'nombre',
            'description',
            'direccion',
            'horario',
            'telefono',
            'correo',
            'serv_origen',
            'serv_destino',
            'latitud',
            'longitud'
        ]

class EmpresaUpdateForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            'nombre',
            'description',
            'direccion',
            'horario',
            'telefono',
            'correo',
            'serv_origen',
            'serv_destino',
            'latitud',
            'longitud'
        ]

class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name'
        ]

class RutaCreateForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = [
            'empresa',
            'nombre',
            'description',
            'costo',
            'horario',
            'duracion_viaje',
            'inclusivo',
            'origen_latitud',
            'origen_longitud',
            'destino_latitud',
            'destino_longitud'
        ]

class RutaUpdateForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = [
            'empresa',
            'nombre',
            'description',
            'costo',
            'horario',
            'duracion_viaje',
            'inclusivo',
            'origen_latitud',
            'origen_longitud',
            'destino_latitud',
            'destino_longitud'
        ]
    
class ParadaCreateForm(forms.ModelForm):
    class Meta:
        model = Parada
        fields = [
            'ruta',
            'nombre',
            'description',
            'horario',
            'latitud',
            'longitud'
        ]

class ParadaUpdateForm(forms.ModelForm):
    class Meta:
        model = Parada
        fields = [
            'ruta',
            'nombre',
            'description',
            'horario',
            'latitud',
            'longitud'
        ]