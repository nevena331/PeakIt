from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Adventure
from users.models import CustomUser as User

from . import serializers

from django.utils.dateparse import parse_date
from django.utils import timezone
from django.db.models import Q


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listAdventures(request):
    if request.method == 'GET':
        query = request.query_params
        location= query.get("location")
        string_date = query.get("date")
        string_keywords = query.get("keywords")
        my_interests = query.get("my_interests")
        
        adventures = Adventure.objects.filter(start_time_and_day__gte = timezone.now())
        
        if location:
            adventures = adventures.filter(location__icontains = location)
        if string_date:
            date = parse_date(string_date)
            adventures = adventures.filter(start_time_and_day__lte = date, 
                                            end_time_and_day__gte = date)
        if string_keywords:
            keywords = string_keywords.split(',')
            keywords_q = Q()
            for keyword in keywords:
                keywords_q |= Q(title__icontains=keyword) | Q(description__icontains=keyword)
            adventures = adventures.filter(keywords_q)
        if my_interests:
            interests_q = Q()
            for interest in request.user.interests:
                interests_q |= Q(activities__icontains = interest)
            adventures = adventures.filter(interests_q)
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

@api_view(['GET', 'PATCH', 'DELETE'])
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
    elif request.method == 'DELETE':
        adventure.delete()
        return Response({"message":"adventure deleted"}, status=status.HTTP_200_OK)