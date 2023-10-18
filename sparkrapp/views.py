from .views_account import sign_up, sign_in
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

def index(request):

    return render(request, "sparkrapp/index.html")


@login_required
def account(request, user_id):

    this_user = request.user

    account = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=account)

    if account.id == this_user.id:

        return render(request, "sparkrapp/account.html", {
            "account": account,
            "profile": profile
        })

    else: 

        return render(request, "sparkrapp/signin.html")


@login_required
def create_profile(request, user_id):

    #if request.method == "POST":
    #pass

    #else:

        return render(request, "sparkrapp/createprofile.html")

