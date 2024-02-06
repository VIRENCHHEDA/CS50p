from numb3rs import validate

def main():
    test_format()
    test_range()


def test_format():
    assert validate(r"25.25.25.25") == True
    assert validate(r"25.25.25") == False
    assert validate(r"25.25") == False
    assert validate(r"25") == False
    assert validate(r"cat") == False



def test_range():
    assert validate(r"512.512.512.512") == False
    assert validate(r"255.255.255.255") == True
    assert validate(r"512.1.1.1") == False
    assert validate(r"1.512.1.1") == False
    assert validate(r"1.1.512.1") == False
    assert validate(r"1.1.1.512") == False
if __name__ == "__main__":
    main()



