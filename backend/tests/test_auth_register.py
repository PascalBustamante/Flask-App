"""Unit tests for api.auth_register API endpoint."""
import os
import sys

topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)

from http import HTTPStatus

from src.models.user import User
from tests.utils import EMAIL, PASSWORD, BAD_REQUEST, register_user
from tests.conftests import app, db

SUCCESS = "successfully registered"
EMAIL_ALREADY_EXISTS = f"{EMAIL} is already registered"


def assert_response(
    response,
    status_code,
    message=None,
    token_type=None,
    expires_in=None,
    access_token=None,
):
    assert response.status_code == status_code
    if message:
        assert "message" in response.json and response.json["message"] == message
    if token_type:
        assert (
            "token_type" in response.json and response.json["token_type"] == token_type
        )
    if expires_in:
        assert (
            "expires_in" in response.json and response.json["expires_in"] == expires_in
        )
    if access_token:
        assert "access_token" in response.json


def test_auth_register(client, db):
    response = register_user(client)
    assert_response(response, HTTPStatus.CREATED, SUCCESS, "bearer", 5, True)
    access_token = response.json["access_token"]
    result = User.decode_access_token(access_token)
    assert result.success
    user_dict = result.value
    assert not user_dict["admin"]
    user = User.find_by_public_id(user_dict["public_id"])
    assert user and user.email == EMAIL


def test_auth_register_email_already_registered(client, db):
    user = User(email=EMAIL, password=PASSWORD)
    db.session.add(user)
    db.session.commit()
    response = register_user(client)
    assert_response(
        response, HTTPStatus.CONFLICT, EMAIL_ALREADY_EXISTS, None, None, False
    )


def test_auth_register_invalid_email(client):
    invalid_email = "first last"
    response = register_user(client, email=invalid_email)
    assert_response(response, HTTPStatus.BAD_REQUEST, BAD_REQUEST, None, None, False)
    assert "errors" in response.json
    assert "password" not in response.json["errors"]
    assert "email" in response.json["errors"]
    assert response.json["errors"]["email"] == f"{invalid_email} is not a valid email"
