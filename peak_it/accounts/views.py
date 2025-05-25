from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
 

from .serializers import RegisterUserSerializer
from users.models import CustomUser as User

def none(request):
    return redirect('register/')

@api_view(["POST"])
def register(request):
    serializer = RegisterUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_201_CREATED)
    
    if User.objects.filter(username=request.data.get("username")).exists():
        return Response({"error": "username already taken"}, status=status.HTTP_418_IM_A_TEAPOT)
    
    if User.objects.filter(email=request.data.get("email")).exists():
        return Response({"error": "email already taken"}, status=status.HTTP_418_IM_A_TEAPOT)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(["POST"])
def logout(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({"ok":"logged out"}, status = status.HTTP_200_OK)
    

