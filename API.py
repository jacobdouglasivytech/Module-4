# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 11:16:49 2023
create python API that meet the CRUD requirments that include ID, book_name, author, publisher
@author: jacob
"""
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(1000))
    author = db.Column(db.String(1000))
    publisher = db.Column(db.String(1000))
    
    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"
    
@app.route('/books')
def get_books():
    books = Book.query.all()
    
    output = []
    for book in books:
        book_data = {'title': book.book_name, 'author': book.author, 'publisher': book.publisher}
        output.append(book_data)
        
    return{"books": output}
@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return ({"title": book.book_name, "author": book.author, "publisher": book.publisher})
   
@app.route('/books', methods=['POST'])
def add_book():
    book = Book(title=request.json['title'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}    

@app.route('/books/<id>', methods=['DELETE'])
def delete_book():
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "deleted"}