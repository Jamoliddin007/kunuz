from rest_framework import serializers
from news.models import MediaFile

class MediaFileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ["id", "media_type", "file", "news"]
