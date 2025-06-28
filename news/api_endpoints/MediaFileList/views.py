from rest_framework.generics import ListAPIView
from news.models import MediaFile
from news.api_endpoints.MediaFileList.serializers import MediaFileListSerializer

class MediaFileListAPIView(ListAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileListSerializer
