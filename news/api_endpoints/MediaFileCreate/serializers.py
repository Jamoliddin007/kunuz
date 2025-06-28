from rest_framework import serializers
from news.models import MediaFile

class MediaFileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ["media_type", "file", "news"]

    def validate_file(self, value):
        max_size = 10 * 1024 * 1024  # 10MB
        if value.size > max_size:
            raise serializers.ValidationError("Fayl hajmi 10MB dan oshmasligi kerak.")
        return value
