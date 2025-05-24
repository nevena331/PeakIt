from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from .models import Adventure
from .serializers import AdventureSerializer

@api_view(['GET'])
def listadventures(request):
    if request.method == 'GET':
        adventures = Adventure.objects.all()
        serializer = AdventureSerializer(adventures, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

