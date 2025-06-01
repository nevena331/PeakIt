from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField

class Adventure (models.Model):

    ACTIVITY_CHOICES = (
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

    title = models.CharField(_("adventure title"), max_length=50, blank = False)
    description = models.TextField(_("description"), blank = False)
    location = models.TextField(_("location"), blank = False)
    creator = models.ForeignKey("users.CustomUser", verbose_name=_("creator"), on_delete=models.CASCADE)
    start_time_and_day = models.DateTimeField(_("start time and day"), auto_now=False, auto_now_add=False, null = False)
    end_time_and_day = models.DateTimeField(_("end time and day"), auto_now=False, auto_now_add=False, null = False)
    activities = MultiSelectField(choices= ACTIVITY_CHOICES, null=False, blank=False)
    passed = models.BooleanField(_("passed"), blank = False)

    def __str__(self):
        return self.title