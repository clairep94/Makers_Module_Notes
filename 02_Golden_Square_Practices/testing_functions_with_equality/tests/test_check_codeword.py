from lib.check_codeword import *

class TestsDemo:
    def test_check_codeword(self):
        assert check_codeword("horse") == "Correct! Come in."
        assert check_codeword("hose") == "Close, but nope."
        assert check_codeword("owijog") == "WRONG!"

'''
CAN ALSO DO:

def test_check_codeword():
    assert check_codeword("horse") == "Correct! Come in."
    assert check_codeword("hose") == "Close, but nope."
    assert check_codeword("owijog") == "WRONG!"

'''