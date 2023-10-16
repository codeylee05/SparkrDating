from django.db import models

MALE = "M"
FEMALE = "F"
BOTH = "B"

GENDERS = [
    (MALE, "MALE"),
    (FEMALE, "FEMALE")
]
PREFERENCES = [
    (MALE, "MALE"), 
    (FEMALE, "FEMALE"),
    (BOTH, "BOTH")
]

class Profile(models.Model):

    user_name = models.CharField(max_length=32)
    user_age = models.IntegerField()
    user_gender = models.CharField(max_length=1, choices=GENDERS)
    user_location = models.CharField(max_length=32)
    user_preference = models.CharField(max_length=1, choices=PREFERENCES)
