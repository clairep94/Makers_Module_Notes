from lib.most_common_letter import *

def test_most_common_letter():
    text = "the roof, the roof, the roof is on fire!"
    assert get_most_common_letter(text) == "o"
