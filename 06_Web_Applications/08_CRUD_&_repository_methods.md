# Linking CRUD, HTTP and Python Repo Class Methods

| CRUD | HTTP Method | Path                  | Python repo method | SQL query                             | 
| -----| ----------- | --------------------- | ------------------ | ------------------------------------- |
|   C  | POST        | `/books`              | `#create`          | `INSERT INTO books VALUES ...`        | 
|   R  | GET         | `/books` or `/books/1`| `#find` & `#all`   | `SELECT * FROM books (WHERE id = ...)`|
|   U  | PATCH       | `/books/1`            | `#update`          | `UPDATE books SET ... WHERE id = ...` |
|   D  | DELETE      | `/books/1`            | `#delete`          | `DELETE FROM books WHERE id = ...`    |

## CRUD APPLICATION:

* **Create**, **Read**, **Update**, **Delete**

## ALL IMPORTS & SET UP:

```shell
git clone https://github.com/makersacademy/web-applications-in-python-project-starter-plain.git YOUR_PROJECT_NAME

cd YOUR_PROJECT_NAME

pipenv install #or install a venv
pipenv shell #or activate venv

createdb project_db
createdb project_db_tests

#open lib/database_connection.py with vs code and plug in new db names

; python seed_dev_database.py
; pytest -sv 
; python app.py
```

```python
# APP.PY
import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.book_repository import BookRepository
from lib.book import Book


# Create a new Flask app
app = Flask(__name__)

```

# ALL SYNTAXES:

[**VIDEO DEMONSTRATION**](https://youtu.be/xBz6_cRfr78?si=nCAfb86TypOxacog&t=3209)

## READ (GET #all):

```python
# GET /books - all
# Return a list of all books in db

# TERMINAL CURL COMMAND
; curl http://localhost:5001/books

# APP.PY
    @app.route('/books', methods=['GET'])
    def get_books():
        connection = get_flask_database_connection(app) #<-- new code
        repository = BookRepository(connection) #<-- new code
        return "\n".join([
            str(book) for book in repository.all()
        ])

# APP_TEST.PY

'''
GET /books
Returns a list of books
'''
def test_get_books(web_client, db_connection): #<-- new code
    db_connection.seed('seeds/book_store.sql') #<-- new code
    response = web_client.get('/books') #<-- new code
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "" \
        "Book(1, Invisible Cities, Italo Calvino)\n" \
        "Book(2, The Man Who Was Thursday, GK Chesterton)\n" \
        "Book(3, Bluets, Maggie Nelson)\n" \
        "Book(4, No Place on Earth, Christa Wolf)\n" \
        "Book(5, Nevada, Imogen Binnie)"

```

## READ (GET #find):

```python
# GET /books/<id> - find
# Return a specific book of a certain id

# TERMINAL CURL COMMAND
; curl http://localhost:5001/books/1

# APP.PY
    @app.route('/books/<id>', methods=['GET'])
    def get_book(id): #<-- new code
        connection = get_flask_database_connection(app) #<-- new code
        repository = BookRepository(connection) #<-- new code
        return str(respository.find(id))

# APP_TEST.PY
'''
GET /books/<id> - find
Returns a specific book of a certain id
'''
def test_get_book(web_client, db_connection): #<-- new code
    db_connection.seed('seeds/book_store.sql') #<-- new code
    response = web_client.get('/books/1') #<-- new code
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "" \
        "Book(1, Invisible Cities, Italo Calvino)"
```


## CREATE (POST #create):

```python
# POST /books
# Creates a new book

# TERMINAL CURL COMMAND
; curl -X POST -d "title=Dave&author_name=Caden%20LoveLace" http://localhost:5001/books
# Note title and author_name are the table column names for books


# APP.PY
@app.route('/books', methods=['POST'])
    def create_book():
        connection = get_flask_database_connection(app) #<-- new code
        repository = BookRepository(connection) #<-- new code
        book = Book(None, request.form['title'], request.form['author_name'])
        book = repository.create(book)
        return "Book added successfully"

# APP_TEST.PY
'''
WHEN: I make a POST request to /books
AND: I send data for a new book with a new Book object
THEN: I should get a 200 response with some variable, and all should return the previous list of books plus the new book.
'''
def test_create_book(web_client, db_connection): #<-- new code
    db_connection.seed('seeds/book_store.sql') #<-- new code
    response = web_client.post('/books', data={ #<-- new code
        'title': 'Dave'
        'author_name': 'Caden LoveLace'
    })
    assert response.status_code == 200
    assert response.data.decoded('utf-8') == 'Book added successfully'

    #repeat test for get_all_books
    response = web_client.get('/books')
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "" \
        "Book(1, Invisible Cities, Italo Calvino)\n" \
        "Book(2, The Man Who Was Thursday, GK Chesterton)\n" \
        "Book(3, Bluets, Maggie Nelson)\n" \
        "Book(4, No Place on Earth, Christa Wolf)\n" \
        "Book(5, Nevada, Imogen Binnie)\n" \
        "Book(6, Dave, Caden LoveLace)"
```

## UPDATE (PATCH #update):


## DELETE (DELETE #delete):
```python
# DELETE /books/<id> 
# Return a specific book of a certain id

# TERMINAL CURL COMMAND
; curl http://localhost:5001/books/1

# APP.PY
    @app.route('/books/<id>', methods=['DELETE'])
    def get_book(id): #<-- new code
        connection = get_flask_database_connection(app) #<-- new code
        repository = BookRepository(connection) #<-- new code
        repository.delete(id)
        return "Book successfully deleted"

# APP_TEST.PY
'''
DELETE /books/<id>
Deletes a specific book of a certain id
'''
def test_get_book(web_client, db_connection): #<-- new code
    db_connection.seed('seeds/book_store.sql') #<-- new code
    response = web_client.get('/books/2') #<-- new code
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Book successfully deleted."

#repeat test for get_all_books
    response = web_client.get('/books')
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "" \
        "Book(1, Invisible Cities, Italo Calvino)\n" \
        "Book(3, Bluets, Maggie Nelson)\n" \
        "Book(4, No Place on Earth, Christa Wolf)\n" \
        "Book(5, Nevada, Imogen Binnie)"
```
