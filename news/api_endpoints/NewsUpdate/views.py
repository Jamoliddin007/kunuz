from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser

from news.models import News
from news.api_endpoints.NewsUpdate.serializers import NewsUpdateSerializer

class NewsUpdateAPIView(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsUpdateSerializer
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]
    lookup_field = "slug"
