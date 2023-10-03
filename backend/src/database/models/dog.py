"""Class definition for User model."""
from datetime import datetime, timezone, timedelta
from uuid import uuid4

from flask import current_app
import jwt
from sqlalchemy.ext.hybrid import hybrid_property

from flask_bcrypt import check_password_hash, generate_password_hash

from sqlalchemy import (
    Integer,
    Column,
    Text,
    String,
    Boolean,
    Table,
    DateTime,
    ForeignKey,
    func,
)
from sqlalchemy.orm import relationship, sessionmaker
from create_app import db_manager
from utils.result import Result

from utils.datetime_util import (
    utc_now,
    get_local_utcoffset,
    make_tzaware,
    localized_dt_string,
)


Base = db_manager.base


dog_breeds = Table(
    "dog_breeds",
    Base.metadata,
    Column("dog_id", Integer, ForeignKey("dogs.id")),
    Column("breed_id", Integer, ForeignKey("breeds.id")),
)


class Dog(Base):
    """Dog model for storing breed and other details."""

    __tablename__ = "dogs"

    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    colors = Column(String)
    age = Column(Integer)
    gender = Column(Boolean)
    size = Column(Integer)
    photos = Column(String)
    contact = Column(String)
    public_id = Column(String(36), unique=True, default=lambda: str(uuid4()))
    breeds = relationship("Breeds", secondary=dog_breeds, back_populates="dogs")


class Breed(Base):
    """Breed model for storing ....."""

    __tablename__ = "breeds"

    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    dogs = relationship("Dog", secondary=dog_breeds, back_populates="breeds")
