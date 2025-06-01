from django.urls import path 
from . import views as userViews
from adventures import views as adventureViews

urlpatterns = [
    path('', userViews.listusers, name = 'list_users'),
    path('<int:pk>/adventures/', adventureViews.listUserAdventures),
    path('<int:pk>', userViews.detailUser, name = 'detail_user'),
    path('my_user/', userViews.editUser, name = 'edit_user')
]
