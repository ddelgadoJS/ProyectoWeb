from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = {
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        }
    
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user


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
            "data-kwimpalastatus": "Alive",
        }
    ))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            "class": "form-control form-control-user",
            "type": "password",
            "placeholder": "Contraseña",
        }
    ))