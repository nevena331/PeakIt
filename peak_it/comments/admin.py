from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('written_on',)

admin.site.register(Comment, CommentAdmin)