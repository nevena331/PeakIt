from django.contrib import admin
from .models import Adventure

class AdventureAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on',)

admin.site.register(Adventure, AdventureAdmin)