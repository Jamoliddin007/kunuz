from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from news.models import Comment


class CommentDeleteAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = "pk"
