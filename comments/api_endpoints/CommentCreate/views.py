from rest_framework.generics import CreateAPIView
from rest_framework import permissions

from comments.models import Comment
from .serializers import CommentCreateSerializer

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
