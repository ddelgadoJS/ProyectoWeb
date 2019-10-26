from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import UserCreateForm, UserLoginForm
from .models import User

# Create your views here.
def user_create_view(request):
    my_form = UserCreateForm()
    if request.method == "POST":
        my_form = UserCreateForm(request.POST)
        if my_form.is_valid():
            User.objects.create(**my_form.cleaned_data)
            return HttpResponseRedirect('/login/')

    context = {
        "form": my_form
    }
    return render(request, "users/user_create.html", context)

def user_login_view(request):
    my_form = UserLoginForm()
    if request.method == "POST":
        my_form = UserLoginForm(request.POST)
        if my_form.is_valid():
            if User.objects.filter(username=my_form.cleaned_data['username']).exists():
                if User.objects.filter(username=my_form.cleaned_data['username'], password=my_form.cleaned_data['password']).exists():
                    return HttpResponseRedirect('/')
                else:
                    messages.add_message(request, messages.ERROR, "Contraseña incorrecta.")
            else:
                messages.add_message(request, messages.ERROR, "Usuario incorrecto.")

    context = {
        "form": my_form
    }
    return render(request, "users/user_login.html", context)