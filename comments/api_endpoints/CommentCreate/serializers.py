from rest_framework import serializers
from comments.models import Comment

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content", "user", "news", "parent"]
