"""Unit tests for User model class."""
from database.models.user import User


def test_encode_access_token(user):
    access_token = user.encode_access_token()
    assert isinstance(access_token, bytes)
