from django.urls import path
from .views import (ProblemListView, ProblemView)

urlpatterns = [
    path("problems/", ProblemListView.as_view(), name="problem-list"),
    path("problems/<int:pk>/", ProblemView.as_view(), name="problem-detail"),
]
