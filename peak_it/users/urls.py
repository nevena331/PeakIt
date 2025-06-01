from django.urls import path 
from . import views as userViews

urlpatterns = [
    path('', userViews.listusers, name = 'list_users'),
    path('<int:pk>', userViews.detailUser, name = 'detail_user'),
    path('my_user/', userViews.editUser, name = 'edit_user')
]
