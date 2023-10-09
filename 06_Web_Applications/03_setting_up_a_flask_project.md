# SETTING UP A FLASK PROJECT

[**VIDEO EXPLANATION**](https://www.youtube.com/watch?v=72JwLuAyHyM)

## FROM SCRATCH:

```shell
; mkdir your_project
; cd your_project
; ls
; pipenv install
; ls
Pipfile Pipfile.lock
; pipenv shell
; pipenv install flask ## Install flask in the pipenv

; nano app.py #makes a file and opens an editor

```

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

```

```shell
; flask run

* Running on http://127.0.0.1:5000 #local server
# Can open a webpage that says "Hello, World!"

; curl http://127.0.0.1:5000
<p>Hello, World!</p>
```

## FROM STARTER:

```shell
# Clone the repository to your local machine
; git clone git@github.com:makersacademy/web-applications-in-python-project-starter-plain.git YOUR_PROJECT_NAME

# Or, if you don't have SSH keys set up
; git clone https://github.com/makersacademy/web-applications-in-python-project-starter-plain.git YOUR_PROJECT_NAME

# Enter the directory
; cd YOUR_PROJECT_NAME

# Install dependencies and set up the virtual environment
; pipenv install

# Activate the virtual environment
; pipenv shell

# Create a test and development database
; createdb YOUR_PROJECT_NAME
; createdb YOUR_PROJECT_NAME_test

# Open lib/database_connection.py and change the database names
# SHIFT TO VS CODE HERE #####
; open lib/database_connection.py

# Seed the development database (ensure you have run `pipenv shell` first)
; python seed_dev_database.py

# Run the tests (with extra logging)
; pytest -sv 

# Run the web server
; python app.py
# Now visit http://localhost:5001/emoji in your browser
```

