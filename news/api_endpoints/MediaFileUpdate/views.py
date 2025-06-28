from rest_framework.generics import UpdateAPIView
from rest_framework import permissions, parsers

from news.models import MediaFile
from news.api_endpoints.MediaFileUpdate.serializers import MediaFileUpdateSerializer

class MediaFileUpdateAPIView(UpdateAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileUpdateSerializer
    permission_classes = [permissions.IsAdminUser]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
