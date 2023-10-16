from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    return render(request, "sparkrapp/index.html")

def sign_up(request):

    #if request.method == "POST": pass | else:
    return render(request, "sparkrapp/signup.html")

def sign_in(request):

    #if request.method == "POST": pass | else:
    return render(request, "sparkrapp/signin.html")