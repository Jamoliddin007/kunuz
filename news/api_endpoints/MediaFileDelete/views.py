from rest_framework.generics import DestroyAPIView
from rest_framework import permissions

from news.models import MediaFile

class MediaFileDeleteAPIView(DestroyAPIView):
    queryset = MediaFile.objects.all()
    permission_classes = [permissions.IsAdminUser]
