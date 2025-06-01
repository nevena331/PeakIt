from rest_framework import serializers
from .models import CustomUser as User

class UserListSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = User
        fields = ['id','username']
    
class UserDetailSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'date_joined', 'birthdate', 'interests']


class UserEditSerializer(serializers.ModelSerializer):
    interests = serializers.MultipleChoiceField(choices=User.INTEREST_CHOICES)

    class Meta:
        model = User  
        fields = ['username', 'first_name', 'last_name', 'email','birthdate', 'interests'] 
