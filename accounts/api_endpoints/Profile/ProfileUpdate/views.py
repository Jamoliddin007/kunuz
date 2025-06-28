from rest_framework.generics import UpdateAPIView
from rest_framework import permissions, parsers
from django.contrib.auth import get_user_model

from accounts.api_endpoints.Profile.ProfileUpdate.serializers import ProfileUpdateSerializer

User = get_user_model()

class ProfileUpdateAPIView(UpdateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = ProfileUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    def get_object(self):
        return self.request.user
