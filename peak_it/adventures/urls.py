from django.urls import path 
from . import views as adventureViews
from comments import views as commentsViews

urlpatterns = [
    path('', adventureViews.listAdventures, name = 'list_adventures'),
    path('<int:post_id>/comments/', commentsViews.adventure_comments, name = 'adventure_comments'),
    path('<int:pk>/', adventureViews.detailAdventure, name = 'detail_adventures'),
    path('edit/<int:pk>/', adventureViews.editAdventure, name = 'edit_adventure'),
    path('create/', adventureViews.createAdventure, name = 'create_adventure')
]
