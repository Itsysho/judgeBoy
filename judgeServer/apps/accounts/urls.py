from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView as LoginView,
    TokenRefreshView,
)
from .views import ProfileView

urlpatterns = [
    path("auth/login", LoginView.as_view(), name="login"),
    path("auth/refresh", TokenRefreshView.as_view(), name="token-refresh"),
    path("auth/profile", ProfileView.as_view(), name="profile"),
]
