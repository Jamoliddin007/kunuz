from rest_framework import serializers
from comments.models import Comment

class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content"]  