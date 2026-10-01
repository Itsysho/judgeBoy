from rest_framework import serializers

from .models import Problem


class ProblemListSerializer(serializers.ModelSerializer):
    """Serializes problem list."""
    class Meta:
        model = Problem
        fields = ["id", "title", "level", "time_stamp"]
        read_only_fields = ["id"]
