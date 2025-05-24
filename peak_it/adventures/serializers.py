from rest_framework import serializers
from .models import Adventure

class AdventureListSerializer (serializers.ModelSerializer):
    class Meta:
        model = Adventure
        fields = ['id', 'title', 'creator', 'time_and_day']

class AdventureDetailSerializer (serializers.ModelSerializer):
    class Meta:
        model = Adventure
        fields = '__all__'
