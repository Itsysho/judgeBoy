from rest_framework.pagination import LimitOffsetPagination


class StandardLimitOffsetPagination(LimitOffsetPagination):
    """Project-wide list pagination with a hard cap on page size."""

    default_limit = 20   # Applied when the client doesn't send ?limit=.
    max_limit = 100      # Client can't exceed this, even if it asks for more.
