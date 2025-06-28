from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from comments.models import Comment
from .serializers import CommentUpdateSerializer

class CommentUpdateAPIView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        # Faqat o'z komentlarini update qilishi uchun
        return self.queryset.filter(user=self.request.user)
