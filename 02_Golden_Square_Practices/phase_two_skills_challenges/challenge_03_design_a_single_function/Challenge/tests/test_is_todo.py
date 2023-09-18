import pytest
from lib.is_todo import is_todo


def test_is_todo_no_todo():
    '''
    Given a string without the substring "#TODO"
    It returns False
    '''
    text = "hello WORLD"
    assert is_todo(text) == False


def test_is_todo_todo():
    '''
    Given a string with the substring "#TODO"
    It returns True
    '''
    text = "#TODO: buy groceries"
    assert is_todo(text) == True


def test_is_todo_todo_lower():
    '''
    Given a string with the substring "#todo"
    It returns True
    '''
    text = "#todo: buy groceries"
    assert is_todo(text) == True


def test_is_todo_wrong_input_type_error():
    '''
    Given a non-string input
    It throws an error
    '''
    text = 9875976
    with pytest.raises(Exception) as e:
        is_todo(text)
    error_message = str(e.value)
    assert error_message == "Error: Invalid input"

