from rest_framework.generics import RetrieveAPIView
from news.models import MediaFile
from news.api_endpoints.MediaFileRetrieve.serializers import MediaFileRetrieveSerializer

class MediaFileRetrieveAPIView(RetrieveAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileRetrieveSerializer
