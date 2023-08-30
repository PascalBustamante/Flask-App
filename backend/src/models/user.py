"""Class definition for User model."""
from datetime import datetime, timezone, timedelta
from uuid import uuid4

from flask import current_app
import jwt
from sqlalchemy.ext.hybrid import hybrid_property

# from .models_old import db
from flask_bcrypt import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy


from utils.datetime_util import (
    utc_now,
    get_local_utcoffset,
    make_tzaware,
    localized_dt_string,
)

db = SQLAlchemy()


class User(db.Model):
    """User model for storing logon credentials and other details."""

    __tablename__ = (
        "cool_user"  # simply because user is a reserved word in many SQL implementations
    )

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    registered_on = db.Column(db.DateTime, default=utc_now)
    admin = db.Column(db.Boolean, default=False)
    public_id = db.Column(db.String(36), unique=True, default=lambda: str(uuid4()))

    def __repr__(self):
        return (
            f"<User email={self.email}, public_id={self.public_id}, admin={self.admin}>"
        )

    @hybrid_property
    def registered_on_str(self):
        registered_on_utc = make_tzaware(
            self.registered_on, use_tz=timezone.utc, localize=False
        )
        return localized_dt_string(registered_on_utc, use_tz=get_local_utcoffset())

    @property
    def password(self):
        raise AttributeError("password: write-only field")

    @password.setter
    def password(self, password):
        log_rounds = current_app.config.get("BCRYPT_LOG_ROUNDS")
        hash_bytes = generate_password_hash(password, log_rounds)
        self.password_hash = hash_bytes.decode("utf-8")

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_public_id(cls, public_id):
        return cls.query.filter_by(public_id=public_id).first()

    def encode_access_token(self):
        now = datetime.now(timezone.utc)
        token_age_h = current_app.config.get("TOKEN_EXPIRE_HOURS")
        token_age_m = current_app.config.get("TOKEN_EXPIRE_MINUTES")
        expire = now + timedelta(hours=token_age_h, minutes=token_age_m)
        if current_app.config["TESTING"]:
            expire = now + timedelta(seconds=5)
        payload = dict(exp=expire, iat=now, sub=self.public_id, admin=self.admin)
        key = current_app.config.get("SECRET_KEY")
        return jwt.encode(payload, key, algorithm="HS256")