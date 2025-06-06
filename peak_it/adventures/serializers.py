from rest_framework import serializers
from .models import Adventure
from users.models import CustomUser as User
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
    participants = serializers.PrimaryKeyRelatedField(many=True,queryset=User.objects.all())

    class Meta:
        model = Adventure
        fields = '__all__'

    def validate(self, data):
        start = data.get('start_time_and_day')
        end = data.get('end_time_and_day')

        if start and end:
            if end < start:
                raise serializers.ValidationError("End date-time must be after start date-time.")

        if start:
            if start < timezone.now():
                raise serializers.ValidationError("Start date-time can not be before now.")

        return data