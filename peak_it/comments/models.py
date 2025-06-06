from django.db import models
from django.utils.translation import gettext_lazy as _

class Comment(models.Model):
    body = models.TextField(_("comment body"), blank=False)
    post = models.ForeignKey("adventures.Adventure", verbose_name=_("post"), on_delete=models.CASCADE)
    writer = models.ForeignKey("users.CustomUser", verbose_name=_("writer"), on_delete=models.CASCADE)
    written_on = models.DateTimeField(_("date"), auto_now=False, auto_now_add=True)


