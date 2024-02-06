import twttr
from twttr import shorten

def test_upper_lower_cases():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("twitter") == "twttr"
    assert shorten("TwiTtEr") == "TwTtr"

def test_num():
    assert shorten("1234") == "1234"

def test_punctuation():
    assert shorten(".,:;") == ".,:;"