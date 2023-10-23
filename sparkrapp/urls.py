from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sign-up/", views.sign_up, name="signup"),
    path("sign-in/", views.sign_in, name="signin"),
    path("account/<int:user_id>/", views.account, name="account"),
    path("create-profile/<int:user_id>/",
         views.create_profile, name="createprofile"),
    path("edit-profile/<int:profile_id>",
         views.edit_profile, name="editprofile"),
    path("sign-out/", views.sign_out, name="signout"),
    path("explore/", views.explore, name="explore")
]
