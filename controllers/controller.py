from flask import render_template, request, redirect
from app import app
from models.book_list import books, add_new_book, delete_book
from models.book import Book

@app.route('/books')
def index():
    return render_template('index.html', title='Home', books=books)

@app.route('/books/<number>')
def book_access(number):
    selected_book = books[int(number)]
    return render_template('book.html', title='Book', book=selected_book)

@app.route('/books', methods=['POST'])
def add_book():
  book_title = request.form['title']
  book_author = request.form['author'] 
  book_genre = request.form['genre']
  book_location = request.form['location']
  books_available = request.form['number']
  book_description = request.form['description']
  new_book = Book(title= book_title, author=book_author, genre=book_genre, location=book_location, number=books_available, description=book_description)
  add_new_book(new_book)
  return redirect('/books')

@app.route('/books/delete/<title>', methods=['POST'])
def delete(title):
  delete_book(title)
  return redirect('/books')


# @app.route('/books', methods=['POST'])
# def add_book():
#   bookTitle = request.form['title']
#   bookAuthor = request.form['author']
#   bookGenre = request.form['genre']
#   # bookLocation = request.form['location']
#   # bookDesc = request.form['description']
#   # bookRecurrence = request.form['recurring']
#   newbook = Book(title=bookTitle, author=bookAuthor, genre=bookGenre)
#   # location=bookLocation, description=bookDesc, recurrence=bookRecurrence)
#   add_new_book(newbook)

#   return render_template('index.html', title='Home', book=books)
