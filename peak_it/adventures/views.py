from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import Adventure
from users.models import CustomUser as User
from . import serializers
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listAdventures(request):
    adventures = Adventure.objects.all()
    serializer = serializers.AdventureListSerializer(adventures, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listUserAdventures(request, pk):
    try:
        user = User.objects.get(pk = pk)
    except user.DoesNotExist: 
        return Response({"message":"User does not exist"}, status= status.HTTP_404_NOT_FOUND)
    
    adventures = Adventure.objects.filter(creator = pk)
    serializer = serializers.AdventureListSerializer(adventures, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)



@api_view (['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def detailAdventure(request, pk):
    try:
        adventure = Adventure.objects.get(pk = pk)
    except adventure.DoesNotExist:
        return Response({"message":"Adventure does not exist"}, status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = serializers.AdventureDetailSerializer(adventure)
        return Response(serializer.data, status = status.HTTP_200_OK)
    if request.method == 'PATCH':
        if request.data.get('message') == 'join':
            adventure.participants.add(request.user)
            adventure.save()
            return Response({"message":"joined"}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createAdventure(request):
    request.data.update({"creator": request.user.id})
    if request.user.id not in request.data.get("participants"):
        request.data.get("participants").append(request.user.id)

    serializer = serializers.AdventureCreateSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH'])
def editAdventure(request, pk):
    try:
        adventure = Adventure.objects.get(pk = pk)
    except adventure.DoesNotExist:
        return Response({"message":"Adventure does not exist"}, status= status.HTTP_404_NOT_FOUND)
    
    if request.user != adventure.creator:
        return Response({"message":"forbidden to access the edit page"}, status=status.HTTP_403_FORBIDDEN)
    
    if request.method == 'GET':
        serializer = serializers.AdventureDetailSerializer(adventure)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = serializers.AdventureCreateSerializer(adventure, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)