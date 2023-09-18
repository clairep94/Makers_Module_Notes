from lib.personal_diary import PersonalDiary


def test_make_snippet_empty_string():
    diary = PersonalDiary()
    assert diary.make_snippet("") == "" #THINK OF EDGE CASES

def test_make_snippet_less_than_five():
    diary = PersonalDiary()
    assert diary.make_snippet("Under five words") == "Under five words"

def test_make_snippet_five_words_long():
    diary = PersonalDiary()
    assert diary.make_snippet("This is five words long") == "This is five words long"

def test_make_snippet_long_string():
    diary = PersonalDiary()
    assert diary.make_snippet("I am testing over five words long") == "I am testing over five..."

def test_count_words_empty_string():
    diary = PersonalDiary()
    assert diary.count_words("") == 0

def test_count_words():
    diary = PersonalDiary()
    assert diary.count_words("How many words?") == 3
