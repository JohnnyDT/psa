from flask import Blueprint, jsonify
from models import books_model

books_blueprint = Blueprint('books', __name__)

# dekorator
# localhost:8080/api/books
@books_blueprint.route('/', methods=['GET'])
def get_all_books():
    return jsonify(book_model.get_books_all(), 200

@books_blueprint.route('/', methods=['GET'])
def get_all_books(id):
    return jsonify(book_model.get_book_by_id(id), 200