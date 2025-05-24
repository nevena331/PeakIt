from django.urls import path 
from . import views as adventureViews

urlpatterns = [
    path('', adventureViews.listAdventures, name = 'list_adventures'),
    path('<int:pk>', adventureViews.detailAdventure, name = 'detail_adventures'),
]
