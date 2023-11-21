#!/usr/bin/python3
"""Book model"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Date, Text, Integer, Table
from sqlalchemy.orm import relationship

book_pages = Table('book_pages', Base.metadata,
                   Column('book_id', String(60), ForeignKey('books.id'),
                          nullable=False, primary_key=True),
                   Column('page_no', Integer,
                          nullable=False, primary_key=True),
                   Column('content', Text, nullable=False)
                   )


class Book(BaseModel, Base):
    """Book class"""
    __tablename__ = 'books'
    book_title = Column(String(128), nullable=False)
    published_date = Column(Date, nullable=False)
    book_summary = Column(Text, nullable=False)
    author_id = Column(String(60), ForeignKey('authors.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes book"""
        super().__init__(*args, **kwargs)
