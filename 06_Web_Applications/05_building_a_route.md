# BUILDING A ROUTE

## ROUTING:

Flask creates a 'routing' table that associates a given request **method** with a given **path** and a block of Python code.

| HTTP Method | Path | Python code                        |
| ----------- | ---- | ---------------------------------- |
| GET         | /    | `# some code to execute`           |
| POST        | /    | `# some different code to execute` |


```python
from flask import Flask

app = Flask(__name__)

# Let's look at an example where Flask receives this request:
# > GET /

# There are a number of routes. We'll look through each one in turn and see if
# it matches.

@app.route('/', methods=['POST'])
def post_index():
    # DOES NOT RUN: The HTTP method (GET) doesn't match the route's (POST)
    return "Not me! :("

@app.route('/hello', methods=['GET'])
def get_hello():
    # DOES NOT RUN: The path (`/hello`) doesn't match the route's (`/`)
    return "Not me either!"

@app.route('/', methods=['GET'])
def get_index():
    # RUNS: This route matches! The code inside the block will be executed now.
    return "I am the chosen one!"

@app.route('/', methods=['GET'])
def other_get_index():
    # DOES NOT RUN: This route also matches, but will not be executed.
    # Only the first matching route (above) will run.
    return "It isn't me, the other route stole the show"
```

## `GET` REQUEST QUERY PARAMETERS:

`request.args` to get the request query parameters

```python
from flask import Flask, request # NOTE: we must import `request` too

app = Flask(__name__)

# Request:
# GET /hello?name=David --> Query param is 'name' = 'David', Path is '/hello'

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name'] # The value is 'David'

    # Send back a friendly greeting with the name
    return f"Hello {name}!"

# To make a request, run:
# curl "http://localhost:5001/hello?name=David"
```

## `POST` REQUEST QUERY PARAMETERS:

`request.form` to send data using _body parameters_

```python
from flask import Flask, request # Remember to import `request`

app = Flask(__name__)

# Request:
# POST /goodbye
#   With body parameter: name=Alice

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'

    # Send back a fond farewell with the name
    return f"Goodbye {name}!"

```