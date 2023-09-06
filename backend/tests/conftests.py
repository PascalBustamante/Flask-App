"""Global pytest fixtures."""
import pytest

from src.create_app import create_app
from src.models.models_old import db
from src.models.user import User
from tests.utils import EMAIL, PASSWORD


@pytest.fixture()
def app():
    app = create_app("testing")
    app.config.update({"TESTING": True})

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def user():
    user = User(email="test_email", username="test_username", password_hash="test_pwd")
