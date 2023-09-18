## 1. Describe the Problem

`As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.`



## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def is_todo(text: str) -> bool:
    '''
    Checks if a text includes the string '#TODO'

    Parameters: text (str)
    eg. "hello WORLD"
    eg. "1209jg9"
    eg. "#TODO: buy groceries


    Returns: bool
    True if string includes "#TODO"
    else False

    Side effects:
    This function doesn't print anything or have any other side-effects.
    '''
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

'''
Given a string without the substring "#TODO"
It returns False
'''
is_todo("No to do here") => False

'''
Given a string with the substring "#TODO"
It returns True
'''
is_todo("#TODO Grocery Shopping") => True

'''
Given a non-string input
It throws an error
'''
is_todo(93408) => "Error: Invalid input"

```

_Encode each example as a test. You can add to the above list as you go._


## 4. Implement the Behaviour


