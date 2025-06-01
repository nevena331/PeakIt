from rest_framework import serializers
from .models import Adventure
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class AdventureListSerializer (serializers.ModelSerializer):
    class Meta:
        model = Adventure
        fields = ['id', 'title', 'creator', 'start_time_and_day', 'end_time_and_day','location']

class AdventureDetailSerializer (serializers.ModelSerializer):
    class Meta:
        model = Adventure
        fields = '__all__'

class AdventureCreateSerializer(serializers.ModelSerializer):
    activities = serializers.MultipleChoiceField(choices=Adventure.ACTIVITY_CHOICES)
    class Meta:
        model = Adventure
        fields = '__all__'

    def validate(self, data):
        if data['end_time_and_day'] < data['start_time_and_day']:
            raise serializers.ValidationError("End date-time must be after start date-time.")
        
        if data['start_time_and_day'] < timezone.now():
            raise serializers.ValidationError("Start date-time can not be before now.") 
        
        return data 