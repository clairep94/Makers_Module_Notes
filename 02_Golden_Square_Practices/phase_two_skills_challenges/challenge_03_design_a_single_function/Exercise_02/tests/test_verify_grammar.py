
from lib.verify_grammar import verify_grammar

def test_not_capitalised():
    text = "this is not capitalised"
    assert verify_grammar(text) == False

def test_no_punctuation():
    text = "This is not punctuated"
    assert verify_grammar(text) == False

def test_wrong_punctuation():
    text = "This is punctuated wrong*"
    assert verify_grammar(text) == False

