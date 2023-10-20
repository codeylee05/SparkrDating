from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .models import Profile

existing_account = "This account already exists. Try signing in?"
non_matching_passwords = "The passwords dont match. Try again"
non_existing_account = "Incorrect email or password. Try signing up?"


def sign_up(request):

    if request.method == "POST":

        email = request.POST["email"]
        password1 = request.POST["password"]
        password2 = request.POST["password2"]

        if password1 == password2:

            users = User.objects.filter(email=email)
            if users:

                 return render(request, "sparkrapp/signup.html", {
                    "message": existing_account
                 })

            else: 
                new_user = User.objects.create_user(email=email, username=email, password=password1)
                new_user.save()

                return render(request, "sparkrapp/signin.html", {
                    "message": "Account created successfully. Let's sign you in"
                })

        else:

            return render(request, "sparkrapp/signup.html", {
                "message": non_matching_passwords
            })

    else:

        return render(request, "sparkrapp/signup.html")


def sign_in(request):

    this_user = request.user

    if request.method == "POST":

        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, username=email, password=password)
        if user is not None:

            login(request, user)

            try: 
                user_profile = Profile.objects.get(user=this_user)
                return redirect("account", user_id=this_user.id)

            except:
                Profile.DoesNotExist
                return redirect("createprofile", user_id=this_user.id)
               
        else:

            return render(request, "sparkrapp/signin.html", {
                "message": non_existing_account
            })

    else:

        return render(request, "sparkrapp/signin.html")
