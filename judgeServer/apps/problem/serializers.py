from rest_framework import serializers

from .models import Problem


class ProblemListSerializer(serializers.ModelSerializer):
    """Serializes problem list."""
    class Meta:
        model = Problem
        fields = ["id", "title", "level", "time_stamp"]
        read_only_fields = ["id"]


class ProblemSerializer(serializers.ModelSerializer):
    """Serializes problem detail."""
    class Meta:
        model = Problem
        fields = ["id", "title", "level", "time_stamp", "src"]
        read_only_fields = ["id"]
