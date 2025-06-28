from rest_framework import serializers
from news.models import News

class NewsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            "title",
            "slug",
            "content",
            "categories",        
            "default_image",
            "images",            
            "is_active",
        ]
        extra_kwargs = {
            "slug": {"required": False},  
        }

    def validate_slug(self, value):
        if not value:
            raise serializers.ValidationError("Slug may not be empty.")
        return value
