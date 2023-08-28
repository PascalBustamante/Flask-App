"""Global pytest fixtures."""
import pytest

from ..create_app import create_app
from ..database.models import db 
from ..database.models.user import User
from tests.utils import EMAIL, PASSWORD


@pytest.fixture
def app():
    app = create_app("testing")
    return app


@pytest.fixture
def db(app, client, request):
    db.drop_all()
    db.create_all()
    db.session.commit()

    def fin():
        db.session.remove()

    request.addfinalizer(fin)
    return db


@pytest.fixture
def user(db):
    user = User(email=EMAIL, password=PASSWORD)
    db.session.add(user)
    db.session.commit()
    return user
