from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from .models import Adventure
from .serializers import AdventureListSerializer, AdventureDetailSerializer

@api_view(['GET'])
def listAdventures(request):
    if request.method == 'GET':
        adventures = Adventure.objects.all()
        serializer = AdventureListSerializer(adventures, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

@api_view (['GET', 'PUT'])
def detailAdventure(request, pk):
    try:
        adventure = Adventure.objects.get(pk = pk)
    except adventure.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AdventureDetailSerializer(adventure)
        print(serializer.data)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = AdventureDetailSerializer(adventure, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)