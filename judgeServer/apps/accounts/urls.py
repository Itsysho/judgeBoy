from django.urls import path

from .views import (LoginView, RefreshView, ProfileView)

urlpatterns = [
    path("auth/login", LoginView.as_view(), name="login"),
    path("auth/refresh", RefreshView.as_view(), name="token-refresh"),
    path("auth/profile", ProfileView.as_view(), name="profile"),
]
