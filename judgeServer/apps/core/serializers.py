from rest_framework import serializers


class ErrorDetailSerializer(serializers.Serializer):
    """One field-level error entry inside error.details."""

    field = serializers.CharField()
    message = serializers.CharField()


class ErrorBodySerializer(serializers.Serializer):
    """The inner `error` object."""

    code = serializers.IntegerField()
    status = serializers.CharField()
    message = serializers.CharField()
    details = ErrorDetailSerializer(many=True, required=False)


class ErrorResponseSerializer(serializers.Serializer):
    """The full error envelope: {"error": {...}}."""

    error = ErrorBodySerializer()
