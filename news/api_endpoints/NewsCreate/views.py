from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from news.models import News
from news.api_endpoints.NewsCreate.serializers import NewsCreateSerializer


class NewsCreateAPIView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer
    permission_classes = [IsAuthenticated]
