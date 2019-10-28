from django import forms
from .models import Empresa

class EmpresaCreateForm(forms.ModelForm):

    nombre = forms.CharField(
        label='Nombre Empresa', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de Empresa'})
        )

    description = forms.CharField(
        label='Descripcion de la empresa', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion de la Empresa'})
        )

    direccion = forms.CharField(
        label='Direccion de la Empresa', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Direccion de la Empresa'})
        )

    horario = forms.CharField(
        label='Horario de la Empresa', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Horario de la Empresa'})
        )

    telefono = forms.CharField(
        label='Telefono de la Empresa', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono de la Empresa'})
        )

    correo = forms.EmailField(
        label='Correo de la Empresa', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo de la Empresa'})
        )

    class Meta:
        model = Empresa
        fields = ['nombre', 'description', 'direccion', 'horario', 'telefono', 'correo', 'serv_origen', 'serv_destino', 'latitud', 'longitud',]