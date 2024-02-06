from um import count

def main():
    test_case()
    test_word_containing_um()



def test_case():
    assert count("um?") == 1
    assert count("Um, thanks for the album. ") == 1
    assert count("Um, thanks, um... ") == 2


def test_word_containing_um():
    assert count("yummy") == 0





