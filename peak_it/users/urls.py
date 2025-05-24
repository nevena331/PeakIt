from django.urls import path 
from . import views as userviews

urlpatterns = [
    path('', userviews.listusers, name = 'list_users'),
]
