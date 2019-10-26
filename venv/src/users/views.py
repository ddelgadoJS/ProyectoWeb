from django.shortcuts import render

from .forms import UserForm, RawUserForm
from .models import User

# Create your views here.
def user_create_view(request):
    my_form = RawUserForm()
    if request.method == "POST":
        my_form = RawUserForm(request.POST)
        if my_form.is_valid():
            User.objects.create(**my_form.cleaned_data)
            my_form = RawUserForm()

    context = {
        "form": my_form
    }
    return render(request, "users/user_create.html", context)