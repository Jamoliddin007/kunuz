from rest_framework import serializers
from news.models import Comment
from accounts.models import User


class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "user", "news", "parent", "content", "created_at"]
