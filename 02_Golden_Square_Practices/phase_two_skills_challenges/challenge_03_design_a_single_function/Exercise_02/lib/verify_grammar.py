# User Story:
    # As a user
    # So that I can improve my grammar
    # I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

import string

def verify_grammar(text: str) -> bool:
    '''
    Params: Text as a string to verify.
    Return: True if text starts with a capital letter AND ends with a suitable sentence-ending punctuation mark.
    '''
    punctuations = [".", "!", "?"]
    
    #Verify if text starts with a capital letter:
    if text[0] in string.ascii_uppercase and text[-1] in punctuations:
        return True
    else:
        return False