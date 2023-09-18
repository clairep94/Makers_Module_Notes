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
    
    # Catch error if text is not a string
    if type(text) != str:
        raise Exception("Error: Invalid input")

    # Convert string to .lower() to catch when all cases of "#TODO" are in the string.    
    substring = "#todo"
    text = text.lower()

    # If substring "#TODO", "#ToDo", "#todo", etc. are in text, return True; else False.
    if substring in text:
        return True
    else:
        return False




