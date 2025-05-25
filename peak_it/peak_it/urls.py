from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include ("users.urls")),
    path('adventures/', include ("adventures.urls")),
    path('accounts/', include ("accounts.urls")), 
    path('', views.homeview)
]
