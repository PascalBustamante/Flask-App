"""Unit tests for api.auth_register API endpoint."""
import os
import sys

topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)

from http import HTTPStatus
import pytest


from src.database.models.user import User
from tests.utils import EMAIL, PASSWORD, BAD_REQUEST, USERNAME, register_user
from tests.conftests import app, db, test_client, _connection, _scoped_session

SUCCESS = "successfully registered"
EMAIL_ALREADY_EXISTS = f"{EMAIL} is already registered"

"""
def test_register_user(test_client):
    # Define test data
    email = "test@example.com"
    username = "testuser"
    password = "testpassword"

    # Call the register_user function to simulate a registration request
    response = test_client.post(
        "/api/v1/auth/register",
        data=f"email={email}&username={username}&password={password}",
        content_type="application/x-www-form-urlencoded",
    )

    # Verify the response
    assert (
        response.status_code == 201
    )  # Assuming a successful registration returns status code 201 (Created)

    # Optionally, you can also check the response content if your application returns data upon registration
    response_data = response.json  # Assuming your response is in JSON format
    print(response_data)
    assert "id" in response_data
    assert "email" in response_data
    assert "username" in response_data
    assert "role" in response_data
"""


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


def test_auth_register(test_client, db):
    response = register_user(test_client)
    assert_response(response, HTTPStatus.CREATED, SUCCESS, "bearer", 5, True)
    access_token = response.json["access_token"]
    result = User.decode_access_token(access_token)
    assert result.success
    user_dict = result.value
    assert not user_dict["admin"]
    test = user_dict["public_id"]
    user = db.session.query(User).filter_by(public_id=test).first()
    print(user)
    # user = User.find_by_public_id(user_dict["public_id"])   #context isssue here
    assert user and user.email == EMAIL


def test_auth_register_email_already_registered(test_client, db):
    user = User(email=EMAIL, username=USERNAME, password_hash=PASSWORD)
    db.session.add(user)
    db.session.commit()
    response = register_user(test_client)
    assert_response(
        response, HTTPStatus.CONFLICT, EMAIL_ALREADY_EXISTS, None, None, False
    )


def test_auth_register_invalid_email(test_client):
    invalid_email = "first last"
    response = register_user(test_client, email=invalid_email)
    assert_response(response, HTTPStatus.BAD_REQUEST, BAD_REQUEST, None, None, False)
    assert "errors" in response.json
    assert "password" not in response.json["errors"]
    assert "email" in response.json["errors"]
    assert response.json["errors"]["email"] == f"{invalid_email} is not a valid email"
