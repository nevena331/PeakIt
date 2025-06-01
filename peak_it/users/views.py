from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import HttpResponse
from .models import CustomUser as User
from . import serializers

@api_view(['GET'])
def listusers(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = serializers.UserListSerializer(users, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

@api_view (['GET'])
@permission_classes([IsAuthenticated])
def detailUser(request, pk):
    try:
        user = User.objects.get(pk = pk)
    except user.DoesNotExist:
        return Response({"message":"User does not exist"}, status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = serializers.UserDetailSerializer(user)
        return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def editUser(request):
    try:
        user = User.objects.get(username = request.user)
    except User.DoesNotExist: 
        return Response({"message":"User does not exist"}, status= status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.UserDetailSerializer(user)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'PUT':
        print("RAW REQUEST DATA:", request.data)
        serializer = serializers.UserEditSerializer(user, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    