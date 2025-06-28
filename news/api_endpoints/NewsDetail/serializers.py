from rest_framework import serializers
from news.models import News

class NewsRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
