import plates
from plates import is_valid



# All vanity plates must start with at least two letters
def test_start_2letters():
    assert is_valid("AA") == True
    assert is_valid("a3hf") == False
    assert is_valid("3c") == False
    assert is_valid("4536") == False


# vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
def test_max_min_char():
    assert is_valid("AB") == True
    assert is_valid("abcdef") == True
    assert is_valid("a") == False
    assert is_valid("abcdefgh") == False


# Numbers cannot be used in the middle of a plate; they must come at the end
def test_no_num_in_middle():
    assert is_valid("AC45XS") == False
    assert is_valid("a23k") == False
    assert is_valid("ab45") == True
    assert is_valid("abcd") == True


# The first number used cannot be a ‘0’.”
def test_no_zero_as_1st_num():
    assert is_valid("0") == False
    assert is_valid("0AAgd") == False
    assert is_valid("asc50") == True
    assert is_valid("as05") == False
    assert is_valid("abcd") == True



# No periods, spaces, or punctuation marks are allowed.
def test_wo_punctuation():
    assert is_valid("ac?df") == False
    assert is_valid("av fd") == False
    assert is_valid("ABCD45") == True
    assert is_valid("ad,") == False
    assert is_valid("anv.jf") == False

