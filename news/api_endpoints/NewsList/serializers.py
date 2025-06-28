from rest_framework import serializers
from news.models import News


class NewsListSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.get_full_name", read_only=True)

    class Meta:
        model = News
        fields = [
            "id",
            "title",
            "slug",
            "author_name",
            "default_image",
            "is_active",
            "views_count",
            "publish_at",
        ]
