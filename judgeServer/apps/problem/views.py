from django.db.models import QuerySet
from drf_spectacular.utils import extend_schema
from rest_framework.generics import (ListAPIView, RetrieveAPIView)
from rest_framework.permissions import AllowAny

from apps.core.openapi import (
    VALIDATION_ERROR_RESPONSE,
    NOT_FOUND_RESPONSE,
    CONFLICT_RESPONSE,
    INTERNAL_RESPONSE
)

from .models import Problem
from .serializers import (ProblemListSerializer, ProblemSerializer)


@extend_schema(
    summary="Get Problem list",
    description="Return the List of problem.",
    responses={
        200: ProblemListSerializer,
        400: VALIDATION_ERROR_RESPONSE,
        404: NOT_FOUND_RESPONSE,
        409: CONFLICT_RESPONSE,
        500: INTERNAL_RESPONSE,
    },
)
class ProblemListView(ListAPIView):
    """Return the List of problem."""

    serializer_class = ProblemListSerializer
    # Problem list is public — any visitor can browse available problems.
    permission_classes = [AllowAny]

    def get_queryset(self) -> QuerySet[Problem]:
        level = self.request.query_params.get('level')

        queryset = Problem.objects.filter(public_status=1)
        if level:
            return queryset.filter(level=level)

        return queryset


@extend_schema(
    summary="Get Problem detail",
    description="Return current problem detail with id.",
    responses={
        200: ProblemSerializer,
        400: VALIDATION_ERROR_RESPONSE,
        404: NOT_FOUND_RESPONSE,
        409: CONFLICT_RESPONSE,
        500: INTERNAL_RESPONSE,
    },
)
class ProblemView(RetrieveAPIView):
    """Return the problem."""

    serializer_class = ProblemSerializer
    permission_classes = [AllowAny]

    queryset = Problem.objects.filter(public_status=1)
