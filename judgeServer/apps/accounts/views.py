from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserProfileSerializer


class ProfileView(RetrieveAPIView):
    """Return the currently authenticated user's profile."""

    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self) -> User:
        # the JWT auth layer already resolved request.user for us
        return self.request.user
