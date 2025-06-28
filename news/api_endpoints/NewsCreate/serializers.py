from rest_framework import serializers
from news.models import News, Category, Tag, MediaFile


class NewsCreateSerializer(serializers.ModelSerializer):
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), many=True, write_only=True
    )
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True, write_only=True, required=False
    )
    image_ids = serializers.PrimaryKeyRelatedField(
        queryset=MediaFile.objects.all(), many=True, write_only=True, required=False
    )

    class Meta:
        model = News
        fields = [
            "title", "slug", "content",
            "category_ids", "tag_ids", "image_ids",
            "default_image", "is_active", "publish_at"
        ]

    def create(self, validated_data):
        categories = validated_data.pop("category_ids", [])
        tags = validated_data.pop("tag_ids", [])
        images = validated_data.pop("image_ids", [])
        user = self.context["request"].user

        news = News.objects.create(**validated_data, author=user)
        news.categories.set(categories)
        news.tags.set(tags)
        news.images.set(images)

        return news
