# POST REQUEST:

## CURL

Syntax:

```shell
; curl -X POST -d "key=variable" http://localhost:5001/special_func

#body_params: "key=variable"
#URL: http://localhost:5001
#path: /special_func
```

Example:

```shell
; curl -X POST -d "text=eee" http://localhost:5001/count_vowels
```

## APP.PY

Syntax:

```shell
@app.route('/special_func', methods=['POST'])
def special_func():
    variable = request.form['key'] #gets key from our query above
    return f"This function shows you the variable: {variable}"
```

Example:

```shell
@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    vowels = ['a', 'e', 'i', 'o', 'u']
    text = request.form['text'] #gets eee from our query above
    vowels_in_text = [char for char in text if char in vowels]
    return f'There are {len(vowels_in_text)} vowels in "{text}"'
```

## TEST_APP.PY

Syntax:

```shell
"""
When: I make a POST request to /path
And: I send 'some variable' as the body parameter text
Then: I should get a 200 response with variable
"""
def test_some_function(web_client):
    response = web_client.post('/path', data={'key': 'some variable'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Something done to some variable"

```

Example:

```shell

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
