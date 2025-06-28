from rest_framework.generics import DestroyAPIView
from rest_framework import permissions

from news.models import News

class NewsDeleteAPIView(DestroyAPIView):
    queryset = News.objects.all()
    lookup_field = "slug"
    permission_classes = [permissions.IsAdminUser]
