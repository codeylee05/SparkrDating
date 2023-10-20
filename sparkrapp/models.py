from django.db import models
from django.contrib.auth.models import User

MALE = "M"
FEMALE = "F"
BOTH = "B"

HETERO = "HET"
GAY = "GAY"
LESB = "LES"
BI = "BIS"
PAN = "PAN"
A = "ASE"
DEMI = "DEM"
QUEER = "QUE"
QUEST = "QUS"
PNTS = "NON"

GENDERS = [
    (MALE, "MALE"),
    (FEMALE, "FEMALE")
]
PREFERENCES = [
    (MALE, "MALE"),
    (FEMALE, "FEMALE"),
    (BOTH, "BOTH")
]
SEXUALITIES = [
    (GAY, "Gay"),
    (HETERO, "Heterosexual"),
    (LESB, "Lesbian"),
    (BI, "Bisexual"),
    (PAN, "Pansexual"),
    (A, "Asexual"),
    (DEMI, "Demisexual"),
    (QUEER, "Queer"),
    (QUEST, "Questioning"),
    (PNTS, "Prefer Not To say")
]


class Profile(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_profile", default=1)
    user_name = models.CharField(max_length=32)
    user_age = models.IntegerField()
    user_gender = models.CharField(max_length=1, choices=GENDERS)
    user_location = models.CharField(max_length=32)
    user_preference = models.CharField(max_length=1, choices=PREFERENCES)
    user_sexuality = models.CharField(
        max_length=3, choices=SEXUALITIES, default=PNTS)
    user_bio = models.TextField(null=True, blank=True)

    def is_valid_Profile(self):

        return self.user and self.user_name and self.user_gender and self.user_location and self.user_preference and self.user_sexuality != "" and int(self.user_age) > 0
