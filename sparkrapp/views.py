from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Profile

def index(request):

    return render(request, "sparkrapp/index.html")


def sign_up(request):

    if request.method == "POST":

        email = request.POST["email"]
        password1 = request.POST["password"]
        password2 = request.POST["password2"]

        if password1 == password2:

            new_user = User.objects.create_user(email=email, username=email, password=password1)
            new_user.save()

            return render(request, "sparkrapp/signin.html", {
                "message": "Account created successfully"
            })

        else:

            return render(request, "sparkrapp/signup.html", {
                "message": "Passwords do not match"
            })

    else:

        return render(request, "sparkrapp/signup.html")


def sign_in(request):

    if request.method == "POST":

        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, username=email, password=password)
        if user is not None:

            login(request, user)
            return render(request, "sparkrapp/account.html")

        else:

            return render(request, "sparkrapp/signin.html", {
                "message": "This account does not exist"
            })

    else:

        return render(request, "sparkrapp/signin.html")


def account(request):

    return render(request, "sparkrapp/account.html")

