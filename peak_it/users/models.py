from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField

class CustomUser(AbstractUser):
    INTEREST_CHOICES = (
        ("hiking", "Hiking"), 
        ("running", "Running"),
        ("biking", "Mountain biking"), 
        ("cycling", "Cycling"),
        ("skiing", "Downhill skiing"),
        ("cross-country", "Cross-country skiing"),
        ("indoor-climbing", "Indoor Climbing"),
        ("outdoor-climbing", "Outdoor Climbing"), 
        ("wind-surfing", "Wind Surfing"), 
        ("camping", "Camping")
    )
    email = models.EmailField(unique=True, null=True, blank=True)

    birthdate = models.DateField(_("date of birth"), auto_now=False, auto_now_add=False, null=True, blank=True)
    interests = MultiSelectField(choices= INTEREST_CHOICES, null=True, blank=True)
    #pfp


