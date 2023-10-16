from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sign-up/", views.sign_up, name="signup"),
    path("account/", views.account, name="account"),
    path("sign-in/", views.sign_in, name="signin")
]