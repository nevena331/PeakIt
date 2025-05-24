from django.urls import path, include 
from . import views as userviews

urlpatterns = [
    path('', userviews.listusers),
]
