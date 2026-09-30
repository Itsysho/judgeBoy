from django.db.models import QuerySet
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.core.openapi import (
    VALIDATION_ERROR_RESPONSE,
    UNAUTHENTICATED_RESPONSE,
    PERMISSION_DENIED_RESPONSE,
    NOT_FOUND_RESPONSE,
    CONFLICT_RESPONSE,
    INTERNAL_RESPONSE
)

from .models import Problem
from .serializers import ProblemListSerializer


@extend_schema(
    summary="Get Problem list",
    description="Return the List of problem.",
    responses={
        200: ProblemListSerializer,
        400: VALIDATION_ERROR_RESPONSE,
        401: UNAUTHENTICATED_RESPONSE,
        403: PERMISSION_DENIED_RESPONSE,
        404: NOT_FOUND_RESPONSE,
        409: CONFLICT_RESPONSE,
        500: INTERNAL_RESPONSE,
    },
)
class ProblemListView(ListAPIView):
    """Return the List of problem."""

    serializer_class = ProblemListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self) -> QuerySet[Problem]:
        level = self.request.query_params.get('level')

        if level:
            return Problem.objects.filter(level=level)

        return Problem.objects.all()
