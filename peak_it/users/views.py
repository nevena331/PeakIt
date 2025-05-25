from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.http import HttpResponse
from .models import CustomUser
from .serializers import CustomUserSerializer

@api_view(['GET'])
def listusers(request):
    if request.method == 'GET':
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

