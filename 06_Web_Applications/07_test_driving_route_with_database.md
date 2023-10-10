# TEST-DRIVING ROUTES THAT INTERACT WITH A DATABASE:

## GET & DELETE:

To specify the id, we need a new parameter called a 'path' parameter (`<something>` placeholder in our route)

```shell
@app.route('/books/<id>')    # <-- New code!
def get_book(id):            # <-- New code!
     # Use id to retrieve the corresponding
     # book from the database.
     return f"Later I'll write the code to get book {id}."

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
     # Use id to delete the corresponding
     # book from the database.
     return f"Later I'll write the code to delete book {id}."
```

## CONNECTING APP.PY & REPOSITORY CLASS:

```shell
from lib.database_connection import get_flask_database_connection  # <-- New code!
from lib.book_repository import BookRepository
from flask import request

app = Flask(__name__)                                              # <-- New code!

@app.route('/books', methods=['GET'])
def get_books():
    connection = get_flask_database_connection(app)                # <-- New code!
    repository = BookRepository(connection)                        # <-- New code!
    repository.all()
    [...]
```

## TIP FOR WRITING TESTS:

Write whole test then, write the following to make sure corresponding route is correct.

```python
@app.route('/path/<id>', methods=['METHOD'])
def some_method(id if there is id):
     connection = BookRepository(connection)
     repository = BookRepository(connection)
     return ""
```

``` shell
; pypenv shell
; python app.py
; pytest -svx

```