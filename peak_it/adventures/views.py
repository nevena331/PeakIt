from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import Adventure
from . import serializers
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listAdventures(request):
        adventures = Adventure.objects.all()
        serializer = serializers.AdventureListSerializer(adventures, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)


@api_view (['GET'])
@permission_classes([IsAuthenticated])
def detailAdventure(request, pk):
    try:
        adventure = Adventure.objects.get(pk = pk)
    except adventure.DoesNotExist:
        return Response({"message":"Adventure does not exist"}, status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = serializers.AdventureDetailSerializer(adventure)
        return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET', 'PUT'])
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
    elif request.method == 'PUT':
        serializer = serializers.AdventureEditSerializer(adventure, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)