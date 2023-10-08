# WRITING TESTS:

## SETTING UP A NEW PROJECT RECAP:

```shell
# MAKE PROJECT DIRECTORY, LIB, TESTS, & INIT FILES #################

# Create Directory
; mkdir your-project-directory
; cd your-project-directory

# Create a folder for your testing files
; mkdir tests
; mkdir lib

# Create module init files in both `tests/` and `lib/` directories
; touch tests/__init__.py
; touch lib/__init__.py

# -----------------------------------

# INSTALL PYTEST #################

# Make sure to be in your-project-directory, containing tests and lib
; pwd 
; ls

# Install pytest using pipenv
; pipenv install pytest --python 3.11

# Verify your setup by running pytest -- REMEMBER TO SAVE CHANGES BEFORE RUNNING!
; pipenv run pytest -x
# ... ...


# -----------------------------------

# CREATE LOCAL & REMOTE REPOS & LINK #############

# Create a repository for your changes
; git init .
; git add .
; git commit -m "Project setup"


# Then go and create a repository on github.com
# On the next screen after you have created the repository,
# follow the "Push an existing repository from the command line" section
# To push your project to your github repository
# It will look something like this...
; git remote add origin YOUR_REMOTE_ADDRESS
; git branch -M main
; git push -u origin main


# -----------------------------------

# PUSHING/PULLING TO REMOTE & CLONING #############

# Push
; git status
; git add <file name>
; git commit -m "description of change"
; git push -u origin main

# Pull
; git pull origin main


# Clone
; cd projectFolder
; git remote add origin <YOUR REPOSITORY ADDRESS HERE>


# REMOVING PYENV OR GIT ##################

# Pyenv:
; pipenv --rm` to remove

# Git:
; rm -rf .git
```


==========================================================

## TESTING FUNCTIONS WITH EQUALITY:

For each `file.py` in `lib`:
We need a `test_file.py` in `tests`

NOTE: for file paths, file.py is run as though it is in the parent folder your_project_folder

* This will contain:

```
.
├── Pipfile
├── Pipfile.lock
├── lib
│   ├── __init_.py
│   └── greet.py
└── tests
    ├── __init__.py
    └── test_greet.py
└── any images or supplemental files for your project.
```


**Suppose we have the following files within `lib`**

```shell
# File: lib/greet.py
def greet(name):
    return f"Hello, {name}!"

# File: lib/check_codeword.py
def check_codeword(codeword):
    if codeword == "horse":
        return "Correct! Come in."
    elif codeword[0] == "h" and codeword[-1] == "e":
        return "Close, but nope."
    else:
        return "WRONG!"

# File: lib/report_length.py
def report_length(str):
    length = len(str)
    return f"This string was {length} characters long."

```

**We then need the following in `test files` within `tests`**

```shell
#File: tests/test_greet.py
from lib.greet import *

def test_greet():
    assert greet("Claire") == "Hello, Claire!"


#File: tests/test_check_codeword.py
from lib.check_codeword import *

def test_check_codeword():
    assert check_codeword("horse") == "Correct! Come in."
    assert check_codeword("hose") == "Close, but nope."
    assert check_codeword("owijog") == "WRONG!"


#File: tests/test_report_length.py
from lib.report_length import *

def test_report_length():
    assert report_length("Claire Peng") == "This string was 11 characters long."
    assert report_length("Makers") == "This string was 6 characters long."
```

==========================================================

## TESTING CLASSES WITH EQUALITY:

```shell
# File: lib/reminder.py

class Reminder:
    def __init__(self, name):
        self.name = name

    def remind_me_to(self, task):
        self.task = task

    def remind(self):
        return f"{self.task}, {self.name}!"
```

```shell
# File: tests/test_reminder.py

from lib.reminder import *

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Kay")
    reminder.remind_me_to("Walk the dog")
    result = reminder.remind()
    assert result == "Walk the dog, Kay!"

# We would typically have a number of these examples.
```


==========================================================

## TESTING CATCHING ERRORS:

**There are two ways to catch errors with pytest:**

* The first is when the main function `returns` an error using an if/else loop or try/except with `return` instead of `raise`, in case you can test the way that we usually test.

```shell
# File: lib/reminder.py -- If Else Loop

class Reminder:
    def __init__(self, name):
        self.name = name
        self.task = None

    def remind_me_to(self, task):
        self.task = task

    def remind(self):
        if self.task is None: #catch error
            return "No reminder set!"
        else:
            return f"{self.task}, {self.name}!"
    
    def remind2(self):
        try: 
            return f"{self.task}, {self.name}!"
        except KeyError:
            return KeyError: "No reminder set!" #test this, do I include KeyError?
        
```
```shell
# File: tests/test_reminder.py

from lib.reminder import *


def test_reminder():
    reminder = Reminder("Kay")
    result = reminder.remind()
    assert result == "No reminder set!"
    assert reminder.remind2() == KeyError: "No reminder set!"  #test this, do I include KeyError?
```
<hr>

**The second way to catch errors with `raise`:**

* The second way is to `raise` an error. We can name the error, and this can be used in if/else (see first example, don't need to include else); or try/except (see second example)

1. We import `pytest` so we can use it to check for errors.
2. We use with `pytest.raises(Exception) as e:` to set up a section of the code where we expect an error to happen and then be caught by pytest.
3. We use `str(e.value)` to get the error message that was generated, and then assert that it is the correct one.

```shell
# File: lib/reminder.py -- Example 1

class Reminder:
    def __init__(self, name):
        self.name = name
        self.task = None

    def remind_me_to(self, task):
        self.task = task

    def remind(self):
        # Look here! We want to fail if there is no reminder yet.
        if self.task is None:
            raise Exception("No reminder set!")
        return f"{self.task}, {self.name}!"
```
```shell
# File: tests/test_reminder.py -- Example 1

import pytest # <-- New code
from lib.reminder import *


def test_reminder():
    reminder = Reminder("Kay")
    with pytest.raises(Exception) as e: # <-- New code
        reminder.remind()
    error_message = str(e.value) # <-- New code
    assert error_message == "No reminder set!"
```

<br>
<hr>
<br>

```shell
import os  
import math  
import re  
  
  
class InvalidEmailError(Exception):  
    """  
    Raised when an email address is invalid  
    """  
  
    pass  
  
  
def division(a: int | float, b: int | float) -> float | ZeroDivisionError:  
    """  
    Returns the result of dividing a by b  
  
    Raises:  
        ZeroDivisionError: If b is 0  
    """  
    try:  
        return a / b  
    except ZeroDivisionError:  
        raise ZeroDivisionError("Division by zero is not allowed")  
  
  
def square_root(a: int) -> float | ValueError:  
    """  
    Returns the square root of a  
  
    Raises:  
        ValueError: If a is negative  
    """  
    try:  
        return math.sqrt(a)  
    except ValueError:  
        raise ValueError("Square root of negative numbers is not allowed")  
  
  
def delete_file(filename: str) -> None | FileNotFoundError:  
    """  
    Deletes a file  
  
    Raises:  
        FileNotFoundError: If the file does not exist  
    """  
    try:  
        os.remove(filename)  
    except FileNotFoundError:  
        raise FileNotFoundError(f"File {filename} not found")  
  
  
def validate_email(email: str) -> bool | InvalidEmailError:  
    """  
    Validates an email address  
  
    Raises:  
        InvalidEmailError: If the email address is invalid  
    """  
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):  
        return True  
    else:  
        raise InvalidEmailError("Invalid email address")  

```
```shell
import pytest  
from src.assert_examples import (  
    division,  
    square_root,  
    validate_email,  
    delete_file,  
    InvalidEmailError,  
)  
  
  
def test_division_zero_division_error():  
    """  
    Test that a ZeroDivisionError is raised when the second argument is 0  
    """  
    with pytest.raises(ZeroDivisionError) as excinfo:  
        division(1, 0)  
    assert str(excinfo.value) == "Division by zero is not allowed"  
  
  
def test_square_root_value_error():  
    """  
    Test that a ValueError is raised when the argument is negative  
    """  
    with pytest.raises(ValueError) as excinfo:  
        square_root(-1)  
    assert str(excinfo.value) == "Square root of negative numbers is not allowed"  
  
  
def test_delete_file_not_found_error():  
    """  
    Test that a FileNotFoundError is raised when the file does not exist  
    """  
    with pytest.raises(FileNotFoundError) as excinfo:  
        delete_file("non_existent_file.txt")  
    assert str(excinfo.value) == "File non_existent_file.txt not found"  
  
  
def test_validate_email_value_error():  
    """  
    Test that an InvalidEmailError is raised when the email address is invalid  
    """  
    with pytest.raises(InvalidEmailError) as excinfo:  
        validate_email("invalid_email")  
    assert str(excinfo.value) == "Invalid email address"
```
