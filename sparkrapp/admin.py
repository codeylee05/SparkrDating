from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):

    list_display = ["id", "user", "user_name", "user_age", "user_gender", "user_location", "user_preference", "user_sexuality", "user_bio" ]

admin.site.register(Profile, ProfileAdmin)