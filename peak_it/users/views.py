from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import HttpResponse
from .models import CustomUser as User
from . import serializers as userserializers

@api_view(['GET'])
def listusers(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = userserializers.UserListSerializer(users, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

@api_view (['GET'])
@permission_classes([IsAuthenticated])
def detailUser(request, pk):
    try:
        user = User.objects.get(pk = pk)
    except user.DoesNotExist:
        return Response({"message":"User does not exist"}, status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = userserializers.UserDetailSerializer(user)
        return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def editUser(request):
    user = request.user
    if request.method == 'GET':
        serializer = userserializers.UserDetailSerializer(user)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'PATCH':

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
            user.set_password(new_password)
            user.auth_token.delete()
            

        serializer = userserializers.UserEditSerializer(user, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    