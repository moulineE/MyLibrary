#!/usr/bin/python3
""" Index """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/books', strict_slashes=False)
def get_books():
    """ retrieves a list of all books """
    all_books = storage.all_by_cls("Book")
    list_books = []
    for book in all_books.values():
        list_books.append(book.to_dict())
    return jsonify(list_books)


@app_views.route('/books/<book_id>', strict_slashes=False)
def get_book(book_id):
    """ retrieves a book by id """
    book = storage.pub_get("Book", book_id)
    if book is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(book.to_dict())


@app_views.route('/books/<book_id>/<page>', strict_slashes=False)
def get_book_page(book_id, page):
    """ retrieves a book page by id and page """
    chapter = storage.get_chapter(book_id, page)
    if chapter is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify({"content": chapter})