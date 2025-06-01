from rest_framework import serializers
from .models import Adventure

class AdventureListSerializer (serializers.ModelSerializer):
    class Meta:
        model = Adventure
        fields = ['id', 'title', 'creator', 'start_time_and_day', 'end_time_and_day','location']

class AdventureDetailSerializer (serializers.ModelSerializer):
    class Meta:
        model = Adventure
        fields = '__all__'

class AdventureEditSerializer (serializers.ModelSerializer):
    activities = serializers.MultipleChoiceField(choices=Adventure.ACTIVITY_CHOICES)
    class Meta:
        model = Adventure
        fields = '__all__'