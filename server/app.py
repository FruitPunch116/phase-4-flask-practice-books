#!/usr/bin/env python3

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Author, Book, Publisher 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.get('/')
def index():
    return "Hello world"

# write your routes here!
@app.get('/authors/<int:id>')
def author_by_id(id):
    try:
        author = Author.query.filter(Author.id == id).first()
        return jsonify(author.to_dict()), 200
    except:
        return jsonify({'error': 'Author not found'}), 404
    
@app.get('/books')
def all_books():
    books = Book.query.all()
    response = [book.to_dict() for book in books]
    return jsonify(response), 200


@app.post("/books")
def create_book():
    try:
        data = request.json
        new_book = Book(**data)
        db.session.add(new_book)
        db.session.commit()
        return jsonify(new_book.to_dict()), 201
    except:
        return jsonify({'error': 'Invalid data'}), 406
    
@app.delete('/author/<int:id>')
def delete_author(id):
    try:
        author = Author.query.filter(Author.id == id).first()

        for book in author.books:
            db.session.delete(book)

        db.session.delete(author)
        db.session.commit()
        return {}, 204
    except:
        return jsonify( {'error':'Author not found'} ), 404
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
