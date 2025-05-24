from django.urls import path 
from . import views as adventureViews

urlpatterns = [
    path('', adventureViews.listadventures),
]
