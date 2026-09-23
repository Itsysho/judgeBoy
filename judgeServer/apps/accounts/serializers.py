from rest_framework import serializers

from .models import User


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes the current user's public profile."""

    class Meta:
        model = User
        fields = ["uuid", "username", "email", "motto"]
        read_only_fields = ["uuid", "username", "email"]
