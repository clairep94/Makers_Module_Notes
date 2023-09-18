from lib.counter import Counter


def test_counter():
    count = Counter()
    count.add(5)
    result = count.report()
    assert result == "Counted to 5 so far."