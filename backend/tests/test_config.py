"""Unit tests for environment config settings."""
import os
import sys

topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)

import os
from src.create_app import create_app


def test_config_development():
    app = create_app("development")
    assert app.config["SECRET_KEY"] != "open sesame"
    assert not app.config["TESTING"]
    # assert app.config["SQLALCHEMY_DATABASE_URI"] == os.getenv("DATABASE_URL", SQLITE_DEV)
    assert app.config["TOKEN_EXPIRE_HOURS"] == 0
    assert app.config["TOKEN_EXPIRE_MINUTES"] == 15


def test_config_testing():
    app = create_app("testing")
    assert app.config["SECRET_KEY"] != "open sesame"
    assert app.config["TESTING"]
    # assert app.config["SQLALCHEMY_DATABASE_URI"] == SQLITE_TEST
    assert app.config["TOKEN_EXPIRE_HOURS"] == 0
    assert app.config["TOKEN_EXPIRE_MINUTES"] == 0


def test_config_production():
    app = create_app("production")
    assert app.config["SECRET_KEY"] != "open sesame"
    assert not app.config["TESTING"]
    # assert app.config["SQLALCHEMY_DATABASE_URI"] == os.getenv(
    #   "DATABASE_URL", SQLITE_PROD
    # )
    assert app.config["TOKEN_EXPIRE_HOURS"] == 1
    assert app.config["TOKEN_EXPIRE_MINUTES"] == 0
