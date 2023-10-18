from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sign-up/", views.sign_up, name="signup"),
    path("sign-in/", views.sign_in, name="signin"),
    path("account/<int:user_id>/", views.account, name="account"),
    path("create-profile/<int:user_id>/", views.create_profile, name="createprofile")
]