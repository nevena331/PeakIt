from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Comment
from adventures.models import Adventure

from .serializers import CommentListSerializer, CommentCreateSerializer

@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def adventure_comments(request, post_id):
    try:
        post = Adventure.objects.get(id = post_id)
    except post.DoesNotExist:
        return Response({"message":"no such post"}, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        comments = Comment.objects.filter(post = post_id)
        serializer = CommentListSerializer(comments, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'POST':
        
        request.data.update({"writer":request.user.id,
                               "post":post.id})
        serializer = CommentCreateSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "PATCH":
        try:
            comment = Comment.objects.get(id = request.data.get("comment_id"))
        except comment.DoesNotExist:
            return Response({"message":"no such comment"}, status=status.HTTP_400_BAD_REQUEST)
        
        if request.user.id != comment.writer.id:
            print("NO")
            return Response({"message":"not allowed"}, status=status.HTTP_403_FORBIDDEN)

        serializer = CommentCreateSerializer(comment, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            comment = Comment.objects.get(id = request.data.get("comment_id"))
        except comment.DoesNotExist:
            return Response({"message":"no such comment"}, status=status.HTTP_400_BAD_REQUEST)

        if request.user not in (comment.writer, post.creator):
            return Response({"message":"not allowed"}, status=status.HTTP_403_FORBIDDEN)

        comment.delete()
        return Response({"message":"comment deleted"}, status=status.HTTP_200_OK)