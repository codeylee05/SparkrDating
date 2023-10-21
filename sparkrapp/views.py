from .views_account import sign_up, sign_in, sign_out
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

invalid_object = "Please respond to all prompts. Try again"


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

    this_user = request.user

    if request.method == "POST":

        name = request.POST["name"]
        age = request.POST["age"]
        gender = request.POST["gender"]
        preference = request.POST["preference"]
        location = request.POST["location"]
        sexuality = request.POST["sexuality"]
        bio = request.POST["bio"]

        new_profile = Profile(user=this_user, user_name=name, user_age=age, user_gender=gender,
                              user_location=location, user_preference=preference, user_sexuality=sexuality, user_bio=bio)

        if not new_profile.is_valid_Profile():

            return render(request, "sparkrapp/createprofile.html", {
                "message": invalid_object
            })

        else:

            new_profile.save()
            return redirect("account", user_id=this_user.id)

    else:

        return render(request, "sparkrapp/createprofile.html")
