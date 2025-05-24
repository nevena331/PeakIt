from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'date_joined', 'is_active', 'last_login', 'birthdate', 'interests']
