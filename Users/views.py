from django.shortcuts import render, HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.


def LoginView(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        login(request, user)

        return HttpResponseRedirect('/')

    return render(request, "login.html", {"form": form})
