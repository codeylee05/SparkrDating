from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):

    list_display = ["user_name", "user_age", "user_gender", "user_location", "user_preference", ]

admin.site.register(Profile, ProfileAdmin)