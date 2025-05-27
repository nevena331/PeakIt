from rest_framework import serializers
from users.models import CustomUser as User

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  
        fields = ['username', 'first_name', 'last_name', 'email', 'password','birthdate', 'interests'] 

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)