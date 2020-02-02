from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from . import forms


def sign_up(request):
    if request.user.is_authenticated:
        return redirect("main_page/")

    form = forms.SignUpForm()
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign_in')

    return render(request, "sign/sign_up.html", {'form': form})


def sign_in(request):
    if request.user.is_authenticated:
        return redirect("/main_page/")

    form = forms.SignInForm()
    if request.method == "POST":
        form = forms.SignInForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/main_page/")

    return render(request, "sign/sign_in.html", {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponse()
