from rest_framework.generics import CreateAPIView
from rest_framework import permissions, parsers
from news.models import MediaFile
from news.api_endpoints.MediaFileCreate.serializers import MediaFileCreateSerializer

class MediaFileCreateAPIView(CreateAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileCreateSerializer
    permission_classes = [permissions.IsAdminUser]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
