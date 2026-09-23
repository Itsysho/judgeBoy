from drf_spectacular.utils import extend_schema
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.core.openapi import (
    VALIDATION_ERROR_RESPONSE,
    UNAUTHENTICATED_RESPONSE,
    PERMISSION_DENIED_RESPONSE,
    NOT_FOUND_RESPONSE,
    CONFLICT_RESPONSE,
    INTERNAL_RESPONSE
)
from apps.core.serializers import ErrorResponseSerializer

from .models import User
from .serializers import UserProfileSerializer


@extend_schema(
    summary="Login",
    description="Exchange username and password for access and refresh tokens.",
    responses={
        200: TokenObtainPairView().get_serializer_class(),  # simplejwt's own response
        400: VALIDATION_ERROR_RESPONSE,  # missing/invalid fields
        401: UNAUTHENTICATED_RESPONSE,  # wrong credentials
        403: PERMISSION_DENIED_RESPONSE,
        404: NOT_FOUND_RESPONSE,
        409: CONFLICT_RESPONSE,
        500: INTERNAL_RESPONSE,
    },
)
class LoginView(TokenObtainPairView):
    """Obtain a fresh access + refresh token pair."""


@extend_schema(
    summary="Refresh access token",
    description="Exchange a valid refresh token for a new access token.",
    responses={
        200: TokenRefreshView().get_serializer_class(),
        401: UNAUTHENTICATED_RESPONSE,  # invalid or expired refresh token
        403: PERMISSION_DENIED_RESPONSE,
        404: NOT_FOUND_RESPONSE,
        409: CONFLICT_RESPONSE,
        500: INTERNAL_RESPONSE,

    },
)
class RefreshView(TokenRefreshView):
    """Obtain a new access token from a refresh token."""


@extend_schema(
    summary="Get current user's profile",
    description="Returns the profile of the currently authenticated user.",
    responses={
        200: UserProfileSerializer,
        400: VALIDATION_ERROR_RESPONSE,
        401: UNAUTHENTICATED_RESPONSE,
        403: PERMISSION_DENIED_RESPONSE,
        404: NOT_FOUND_RESPONSE,
        409: CONFLICT_RESPONSE,
        500: INTERNAL_RESPONSE,
    },
)
class ProfileView(RetrieveAPIView):
    """Return the currently authenticated user's profile."""

    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self) -> User:
        # the JWT auth layer already resolved request.user for us
        return self.request.user
