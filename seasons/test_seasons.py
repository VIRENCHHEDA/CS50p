from seasons import check_birthday




def test_check_birthday():
    assert check_birthday("2023-12-31") == ("2023", "12", "31")
    assert check_birthday("2021-2-3") == None
    assert check_birthday("october 25,2002") == None



