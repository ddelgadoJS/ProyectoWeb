from django import forms
from .models import User

class UserCreateForm(forms.Form):
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
    email = forms.EmailField(label='', widget=forms.TextInput(
        attrs={
            "class": "form-control form-control-user",
            "type": "text",
            "aria-describedby": "userHelp",
            "placeholder": "Correo",
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

class UserLoginForm(forms.Form):
    username  = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            "class": "form-control form-control-user",
            "type": "text",
            "aria-describedby": "userHelp",
            "placeholder": "Usuario",
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