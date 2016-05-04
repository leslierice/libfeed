import logging, mapper, os
from flask import Flask, render_template, jsonify
from flask.ext.stormpath import StormpathError, StormpathManager, User, login_required, login_user, logout_user, user
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import or_

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
logger.debug("Welcome")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-secret-key'
app.config['STORMPATH_API_KEY_FILE'] = 'apiKey-7AKT19DZWY9492JYEKXNAQ7V0.properties'
app.config['STORMPATH_APPLICATION'] = 'LibFeed'
app.config['STORMPATH_REDIRECT_URL'] = '/newsfeed'
app.config['STORMPATH_ENABLE_MIDDLE_NAME'] = False
app.config['STORMPATH_REGISTRATION_TEMPLATE'] = 'register.html'
app.config['STORMPATH_LOGIN_TEMPLATE'] = 'login.html'

stormpath_manager = StormpathManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:password@localhost/db'
db = SQLAlchemy(app)

from models import *

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/api/current_user', methods=["GET"])
@login_required
def current_user():
    # return jsonify({'user': user.given_name})
    user_test =  Person.query.filter_by(id=2).first()
    borrowed_books = []
    reviews = []
    for f in user_test.friends:
        friend = Person.query.filter_by(id=f.id).first()
        borrowed_books.append(list(map(mapper.library_copy_to_dict, friend.borrowed_books)))
        reviews.append(list(map(mapper.review_to_dict, friend.reviews)))
    return jsonify({'borrowed_books': borrowed_books, 'reviews': reviews})

@app.route('/api/user/<id>', methods=["GET"])
@login_required
def get_user(id):
    return jsonify({'user': mapper.user_to_dict(Person.query.filter_by(id=id).first())})

@app.route('/api/book/<isbn>', methods=["GET"])
@login_required
def get_book(isbn):
    return jsonify({'book': mapper.book_to_dict(Book.query.filter_by(isbn=isbn).first())})

@app.route('/api/library/<id>', methods=["GET"])
@login_required
def get_library(id):
    return jsonify({'library': mapper.library_to_dict(Library.query.filter_by(id=id).first())})

@app.route('/api/search/<search_term>', methods=["GET"])
def search(search_term):
    users = list(map(mapper.user_to_dict, Person.query.filter(Person.name==search_term).all()))
    books = list(map(mapper.book_to_dict, Book.query.filter(or_(Book.title==search_term, Book.author==search_term.lower())).all()))
    libraries = list(map(mapper.library_to_dict, Library.query.filter(Library.name==search_term).all()))
    return jsonify({'users': users, 'books': books, 'libraries': libraries})

@app.route('/', defaults={'path': ''})

@app.route('/<path:path>')
def index(path):
    return render_template('index.html', user=user)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
