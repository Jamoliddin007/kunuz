from rest_framework.generics import RetrieveAPIView
from rest_framework import permissions

from news.models import News
from .serializers import NewsRetrieveSerializer

class NewsRetrieveAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsRetrieveSerializer
    lookup_field = "slug"
    permission_classes = [permissions.AllowAny]
