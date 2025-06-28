from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from news.models import Comment
from .serializers import CommentListSerializer


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.select_related("user", "news", "parent").all()
    serializer_class = CommentListSerializer
    permission_classes = [AllowAny]
