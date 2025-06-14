from django.shortcuts import redirect
from django.contrib.auth.models import update_last_login

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.serializers import ValidationError

from datetime import datetime
from .serializers import RegisterUserSerializer
from users.models import CustomUser as User

def none(request):
    return redirect('register/')

@api_view(["POST"])
def register(request):
    old_password = request.data.get('old_password')
    new_password = request.data.get('new_password')
    confirm_new_password = request.data.get('confirm_new_password')
    if new_password:
        if old_password:
            if confirm_new_password:
                if new_password != confirm_new_password:
                    raise ValidationError("password and confirmation password do not match")
                if not user.check_password(old_password):
                    raise ValidationError("old password incorrect")
            else:
                raise ValidationError("you must enter a confirmation password")
        else:
            raise ValidationError("you must enter a confirmation password")
        del request.data["old_password"]
        del request.data["confirm_new_password"]
        del request.data["new_password"]
    
    serializer = RegisterUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        update_last_login(None, user)
        return Response({"token": token.key}, status=status.HTTP_201_CREATED)
    
    if User.objects.filter(username=request.data.get("username")).exists():
        return Response({"detail": "username already taken"}, status=status.HTTP_418_IM_A_TEAPOT)
    
    if User.objects.filter(email=request.data.get("email")).exists():
        return Response({"detail": "email already taken"}, status=status.HTTP_418_IM_A_TEAPOT)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(["POST"])
def logout(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({"message":"logged out"}, status = status.HTTP_200_OK)

