from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Empresa

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