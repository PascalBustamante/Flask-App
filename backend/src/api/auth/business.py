"""Business logic for /auth API endpoints."""
from http import HTTPStatus

from flask import current_app, jsonify
from flask_restx import abort

from database.models.user import User
from create_app import db_manager as db


def process_registration_request(email, username, password):
    db = current_app.db
    if db.session.query(User).filter_by(email=email).first():
        abort(HTTPStatus.CONFLICT, f"{email} is already registered", status="fail")

    # if User.find_by_email(email):
    #   abort(HTTPStatus.CONFLICT, f"{email} is already registered", status="fail")
    new_user = User(email=email, username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    access_token = new_user.encode_access_token()
    print(access_token)
    response = jsonify(
        status="success",
        message="successfully registered",
        access_token=access_token,
        token_type="bearer",
        expires_in=_get_token_expire_time(),
    )
    response.status_code = HTTPStatus.CREATED
    response.headers["Cache-Control"] = "no-store"
    response.headers["Pragma"] = "no-cache"
    return response


def _get_token_expire_time():
    token_age_h = current_app.config.get("TOKEN_EXPIRE_HOURS")
    token_age_m = current_app.config.get("TOKEN_EXPIRE_MINUTES")
    expires_in_seconds = token_age_h * 3600 + token_age_m * 60
    return expires_in_seconds if not current_app.config["TESTING"] else 5
