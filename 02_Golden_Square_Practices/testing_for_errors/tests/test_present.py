import pytest
from lib.present import Present

def test_wrap_contents():
    gift = Present()
    gift.wrap(contents="New shoes") 
    assert gift.contents == "New shoes"

def test_wrap_already():
    gift = Present()
    gift.wrap(contents="Shoes")
    with pytest.raises(Exception) as e:
        gift.wrap(contents="New present")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."


def test_unwrap_nothing():
    gift = Present()
    with pytest.raises(Exception) as e:
        gift.unwrap()
    error_message = str(e.value)
    assert error_message


def test_unwrap_contents():
    gift = Present()
    gift.wrap(contents="New shoes") 
    assert gift.unwrap() == "New shoes"