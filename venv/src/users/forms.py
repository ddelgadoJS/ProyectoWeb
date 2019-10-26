from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'firstname',
            'lastname',
            'password',
            'email'
        ]

class RawUserForm(forms.Form):
    username  = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            "class": "form-control form-control-user",
            "type": "text",
            "aria-describedby": "userHelp",
            "placeholder": "Usuario",
            "data-kwimpalastatus": "Alive"
        }
    ))
    firstname = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            "class": "form-control form-control-user",
            "type": "text",
            "aria-describedby": "userHelp",
            "placeholder": "Nombre(s)",
            "data-kwimpalastatus": "Alive"
        }
    ))
    lastname = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            "class": "form-control form-control-user",
            "type": "text",
            "aria-describedby": "userHelp",
            "placeholder": "Apellido(s)",
            "data-kwimpalastatus": "Alive"
        }
    ))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            "class": "form-control form-control-user",
            "type": "password",
            "placeholder": "Contraseña",
        }
    ))
    email = forms.EmailField(label='', widget=forms.TextInput(
        attrs={
            "class": "form-control form-control-user",
            "type": "text",
            "aria-describedby": "userHelp",
            "placeholder": "Correo",
            "data-kwimpalastatus": "Alive"
        }
    ))