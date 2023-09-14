from lib.report_length import *

def test_report_length():
    assert report_length("Claire Peng") == "This string was 11 characters long."
    assert report_length("Makers") == "This string was 6 characters long."