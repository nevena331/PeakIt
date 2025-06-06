from rest_framework import serializers
from .models import Comment

class CommentCreateSerializer(serializers.Serializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentListSerializer(serializers.Serializer):
    class Meta:
        model = Comment
        fields = ['id', 'body', 'writer', 'written_on']