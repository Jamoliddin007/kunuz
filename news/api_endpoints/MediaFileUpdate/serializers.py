from rest_framework import serializers
from news.models import MediaFile

class MediaFileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ["media_type", "file", "news"]

    def validate_file(self, value):
        if value and value.size > 5 * 1024 * 1024:
            raise serializers.ValidationError("File size must be less than 5MB.")
        return value
