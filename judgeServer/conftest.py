import pytest
from apps.accounts.models import User

LOGIN_URL = '/api/v1/auth/login'

FAKE_USER = {
    "username": "testuser", "password": "testpass"
}


@pytest.fixture
def create_fake_user():
    user = User.objects.create_user(**FAKE_USER)
    return user
