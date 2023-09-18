from lib.challenge_two import *

#Most of this function was debugged by printing (discover debugging) each step rather than in pytest.

def test_make_cipher():
    assert make_cipher("secretkey") == ['s', 'e', 'c', 'r', 't', 'k', 'y', 'a', 'b', 'd', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'u', 'v', 'w', 'x', 'z']

def test_encode():
    assert encode("theswiftfoxjumpedoverthelazydog", "secretkey") == "EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL"

def test_decode():
    assert decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey") == "theswiftfoxjumpedoverthelazydog"