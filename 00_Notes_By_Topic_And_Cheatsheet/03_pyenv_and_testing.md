# PYTHON:

## PYTEST:
Pytest is a test framework to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

``` shell
# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5
```


## INSTALLING DEPENDENCIES:

System-wide change -- don't need to be in the correct wd. Only need to do once on the machine.

```
; python3 -m ensurepip --upgrade
; pip3 install --user pipenv
; echo 'export PATH="$PATH:$(python3 -m site --user-base)/bin" # Add Pipenv to PATH' >> ~/.zshrc
; source ~/.zshrc
; pipenv --version
pipenv, version ...
```

## SETTING UP TESTS:

### CHECK FOR CORRECT WORKING DIRECTORY:
Make sure to go inside the folder CONTAINING the `lib` folder and `tests` folders before you do this:

``` shell
cd projectFolder

; ls #check that the folder CONTAINS lib and tests folders before initiating pytest
AirQuality.csv Pipfile        Pipfile.lock   conftest.py    lib            tests
```

### SET UP THE TESTING ENVIRONMENT:

``` shell
pipenv install
```

#### TO REMOVE ENVIRONMENT:

If initalised in the wrong directory:

``` shell
pipenv --rm
```

## RUN TEST:

``` shell
#PREFERRED METHOD:
; pipenv run pytest -x # this runs till the first error if in correct wd



#OTHER METHODS:
; pipenv run pytest # this runs through all the tests

; pipenv run pytest test/test_2_classes.py -x #same as preferred method, except if in other wd

; pipenv run python my_file.py # use this to the python file instead of python 3 run my_file.py

```

===============================================================

# SETTING UP A NEW PROJECT:

To set up a new pytest project from scratch:

```shell
# First, create a directory for your project
; mkdir your-project-directory
; cd your-project-directory

# Next, install pytest using pipenv
; pipenv install pytest --python 3.11
# This may take a few minutes

# Create a folder for your testing files
; mkdir tests
; mkdir lib

# Create module init files in both `tests/` and `lib/` directories
; touch tests/__init__.py
; touch lib/__init__.py
# These might seem pointless, but they're important for Python to find
# all of your files.

# Verify your setup by running pytest
; pipenv run pytest
================================ test session starts ================================
platform darwin -- Python 3.1, pytest-7.2.0, pluggy-1.0.0
rootdir: .../your-project-directory
collected 0 items

=============================== no tests ran in 0.01s ===============================

# And create a repository for your changes
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
```
