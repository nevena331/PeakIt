from django.urls import path, include
from django.views.generic.base import RedirectView
from . import views as authViews

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('register/', authViews.register, name = "register"), 
    path('', RedirectView.as_view(url='/accounts/register/', permanent=False)),
    path('login/', obtain_auth_token, name = "login"), 
    path('logout/', authViews.logout, name = "logout"),
]