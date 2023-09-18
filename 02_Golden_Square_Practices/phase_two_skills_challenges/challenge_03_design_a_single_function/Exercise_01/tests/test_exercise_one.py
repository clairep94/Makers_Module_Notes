from lib.exercise_one import reading_time

def test_reading_time_200_words():
    assert reading_time(200) == "It will take 1 minute(s) to read this."

def test_reading_time_50_words():
    assert reading_time(50) == "It will take less than 1 minute to read this."

def test_reading_time_1070_words(): #5.35 min round down.
    assert reading_time(1070) == "It will take 5 minute(s) to read this."

def test_reading_time_1190_words(): #5.96 min round up.
    assert reading_time(1190) == "It will take 6 minute(s) to read this."

def test_reading_time_15000_words(): #75 minutes
    assert reading_time(15000) == "It will take 1 hour(s) and 15 minute(s) to read this."