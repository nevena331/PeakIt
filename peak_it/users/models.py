from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField

from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
from django.utils.translation import gettext_lazy as _
from django.db import models

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
    

    email = models.EmailField(unique=True)
    birthdate = models.DateField(_("date of birth"), null=True, blank=False)
    interests = MultiSelectField(choices=INTEREST_CHOICES, blank=False)
