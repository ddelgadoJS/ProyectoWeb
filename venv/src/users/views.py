from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

from .forms import UserCreateForm, UserLoginForm, RegistrationForm
from .models import User

# Create your views here.
def user_create_view(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    context = {
        "form": form
    }
    return render(request, "users/user_create.html", context)

def user_login_view(request):
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        messages.add_message(request, messages.ERROR, "Datos incorrectos.")
