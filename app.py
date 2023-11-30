#!/usr/bin/python3
""" Flask Application """
from flask import Flask, render_template, make_response, jsonify, request
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from api.v1.views.books import get_books

app = Flask(__name__)
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


@app.route('/mylibrary', strict_slashes=False)
@app.route('/mylibrary/index.html', strict_slashes=False)
def home_page():
    return render_template('index.html')


@app.route('/mylibrary/books', strict_slashes=False)
def all_books():
    all_books = storage.all_by_cls("Book")
    list_books = []
    for book in all_books.values():
        author = storage.pub_get("Author", book.author_id)
        book = book.to_dict()
        book['author_name'] = "{} {}".format(author.first_name, author.last_name)
        list_books.append(book)
    return render_template('index.html', books=list_books)


"""@app.route('/mylibrary/search', strict_slashes=False)
def search():
    results = storage.book_search(request.args.get("q"))

    return jsonify(results)"""

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
