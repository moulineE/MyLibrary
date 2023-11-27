#!/usr/bin/python3
"""DBStorage engine"""

import models
from models.base_model import BaseModel, Base
from models.user import User
from models.author import Author
from models.book import Book
from models.bookmark import Bookmark
from models.opened_book import Opened_book
from models.book_page import Book_page
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

classes = {"User": User, "Author": Author, "Book": Book,
           "Bookmark": Bookmark, "Opened_book": Opened_book,
           "Book_page": Book_page}
pub_classes = {"Author": Author, "Book": Book, "Book_page": Book_page}


class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format('MyLibrary_dev',
                                             'MyLibrary_dev_pwd',
                                             'localhost',
                                             'MyLibrary_dev_db'))

    def all_by_cls(self, cls):
        """Query on the current database session by class name"""
        new_dict = {}
        for clss in pub_classes:
            if cls is pub_classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def get_chapter(self, book_id, page_no):
        """get the chapter of the book"""
        book = self.pub_get(Book, book_id)
        if book is None:
            return None
        if page_no < 1 or page_no > book.chapter_count:
            return None
        chapter = self.__session.query(Book_page).filter_by(
            book_id=book_id, page_no=page_no).first()
        return chapter.content

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """Close the session"""
        self.__session.remove()

    def pub_get(self, cls, id):
        """
        Returns the object based on the class name and its ID,
        or None if not found
        :param cls:
        :param id:
        :return obj or None:
        """
        all_cls = models.storage.all_by_cls(cls)
        for value in all_cls.values():
            if value.id == id:
                return value
        return None

    def count(self, cls):
        """count the number of objects in storage"""
        if cls not in pub_classes.values():
            return None
        else:
            count = len(models.storage.all_by_cls(cls).values())
            return count
