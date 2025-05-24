from django.db import models
from django.utils.translation import gettext_lazy as _


class Adventure (models.Model):
    title = models.CharField(_("adventure title"), max_length=50, blank = False)
    description = models.TextField(_("description"), blank = False)
    location = models.TextField(_("location"), blank = False)
    creator = models.ForeignKey("users.CustomUser", verbose_name=_("creator"), on_delete=models.CASCADE)
    time_and_day = models.DateTimeField(_("time and day"), auto_now=False, auto_now_add=False, null = False)

    def __str__(self):
        return self.title