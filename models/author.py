#!/usr/bin/python3
"""Author model"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import relationship

class Author(BaseModel, Base):
    """Author class"""
    __tablename__ = 'authors'
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    nb_of_books = Column(Integer, nullable=False, default=0)
    books = relationship("Book", backref="author")

    def __init__(self, *args, **kwargs):
        """initializes author"""
        super().__init__(*args, **kwargs)