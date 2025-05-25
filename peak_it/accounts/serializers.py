from rest_framework import serializers
from users.models import CustomUser

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser  
        fields = ['username', 'first_name', 'last_name', 'email', 'password','birthdate', 'interests'] 
