# GET REQUEST:

The `GET` method is often used to _query or retrieve_ information from the server. The exact data returned depends of the implementation of the web server.

A `GET` request can contain _query parameters_, as part of the URL.

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


## CURL

Syntax:

```shell
; curl "http://localhost:5001/special_func?key=variable"

; curl http://localhost:5001/special_func

#query_params: key=variable -- If no query param, no quotes in curl URL
#URL: http://localhost:5001
#path: /special_func
```

Example:

```shell
; curl "http://localhost:5001/greet?person=Kay"

; curl http://localhost:5001/greet

```

## APP.PY

Syntax:

```python
@app.route('/special_func', methods=['GET'])
def special_func():
    variable = request.args['key'] #gets query params
    return f"This function shows you the variable: {variable}"
```

Example:

```python
@app.route('/greet', methods=['POST'])
def greet():
    name = request.args['person']
    return f'Hello {name}!'
```

## TEST_APP.PY

Syntax:

```python
"""
When: I make a GET request to /path
And: I send 'some variable' as the query parameter text
Then: I should get a 200 response with variable
"""
def test_some_function(web_client):
    response = web_client.get('/path?key=variable')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Something done to some variable"

```

Example:

```python

# File: tests/test_app.py

"""
When: I make a GET request to /greet
And: I send 'Diana' as the query parameter text
Then: I should get a 200 response with 'Hello Diana!'
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/greet?person=Diana')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello Diana!'

```


