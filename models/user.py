#!/usr/bin/python3
"""User model"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from hashlib import md5


class User(BaseModel, Base):
    """User class"""
    __tablename__ = 'users'
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    bookmarks = relationship("Bookmark", backref="users",
                             cascade="all, delete")
    opened_books = relationship("Opened_book", backref="users",
                                cascade="all, delete")

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
        self.password = generate_password_hash(kwargs.get('password'))

    def check_password(self, password):
        return check_password_hash(self.password, password)

    """def __setattr__(self, name, value):
        """"""sets a password with md5 encryption""""""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)"""
