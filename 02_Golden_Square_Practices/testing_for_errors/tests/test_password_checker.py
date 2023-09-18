import pytest
from lib.password_checker import PasswordChecker

def test_if_len_is_valid():
    password_checker = PasswordChecker()
    result = password_checker.check("woeiroigno5r2")
    assert result == True

def test_if_len_is_invalid():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("ahahbb")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."