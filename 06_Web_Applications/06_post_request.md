# POST REQUEST:

The `POST` method is often used to _send_ data to the web server (usually to create or update data, or just send some information). What is done with this data depends of the implementation of the web server.

A `POST` request can contain _query parameters_ (like a `GET` request), but it can also contain _body parameters_. Contrarily to _query parameters_, they are not included in the URL, but within the request body itself.


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

## CURL

Syntax:

```shell
; curl -X POST -d "key=variable&other_key=other%20variable" http://localhost:5001/special_func

#body_params: "key=variable", "other_key=other%20variable"
#URL: http://localhost:5001
#path: /special_func
```

Example:

```shell
; curl -X POST -d "text=eee" http://localhost:5001/count_vowels
```

## APP.PY

Syntax:

```python
from flask import Flask, request # Remember to import `request`

app = Flask(__name__)


@app.route('/special_func', methods=['POST'])
def special_func():
    variable = request.form['key'] #gets key from our query above
    return f"This function shows you the variable: {variable}"
```

Example:

```python
from flask import Flask, request # Remember to import `request`

app = Flask(__name__)


@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    vowels = ['a', 'e', 'i', 'o', 'u']
    text = request.form['text'] #gets eee from our query above
    vowels_in_text = [char for char in text if char in vowels]
    return f'There are {len(vowels_in_text)} vowels in "{text}"'
```

## TEST_APP.PY

Syntax:

```python
"""
When: I make a POST request to /path
And: I send 'some variable' as the body parameter text
Then: I should get a 200 response with variable
"""
def test_some_function(web_client):
    response = web_client.post('/path', data={'key': 'some variable', 'other_key': 'other variable'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Something done to some variable"

```

Example:

```python

# File: tests/test_app.py

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

```
