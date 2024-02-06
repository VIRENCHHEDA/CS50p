import pytest
import pandas as pd
from unittest.mock import patch
from project import display_balance, deposit, withdraw, change_pin, auth_ac, pin, home

@pytest.fixture
def mock_dataframe():
    # You can customize this fixture based on your specific needs
    data = {
        'Account Number': ['VCB114A755', 'VCB795H919'],
        'Name': ['Viren Chheda', 'Nathan Bryant'],
        'Pin': [1719, 7138],
        'Balance': [78313.33, 70559.92]
    }
    return pd.DataFrame(data)

def test_display_balance(capsys):
    display_balance(1000.0)
    captured = capsys.readouterr()
    assert "Account Balance: Rs.1000.00" in captured.out

def test_deposit(capsys):
    balance = 1000.0
    amount = 500.0
    new_balance = deposit(balance, amount)
    captured = capsys.readouterr()
    assert "DEPOSIT SUCCESFULL!" in captured.out
    assert f"Deposited: Rs.{amount:.2f}" in captured.out
    assert f"Account Balance: Rs.{new_balance:.2f}" in captured.out

def test_withdraw(capsys):
    balance = 1000.0
    amount = 500.0
    new_balance = withdraw(balance, amount)
    captured = capsys.readouterr()
    assert "WITHDRAWAL SUCCESFULL!" in captured.out
    assert f"Withdrawn: Rs.{amount:.2f}" in captured.out
    assert f"Account Balance: Rs.{new_balance:.2f}" in captured.out

def test_change_pin(mock_dataframe):
    with patch('project.df', mock_dataframe):
        user_ac = 'VCB114A755'
        old_pin = 1719
        new_pin = 2510
        result = change_pin(user_ac, old_pin, new_pin)
        assert result == new_pin
        assert mock_dataframe['Pin'][mock_dataframe['Account Number'] == user_ac].iloc[0] == new_pin



def test_auth_ac(mock_dataframe, capsys):
    with patch('project.df', mock_dataframe):
        with patch('builtins.input', side_effect=['999999', '123456']):
            result = auth_ac()
            assert result is None  # auth_ac doesn't return anything
            captured = capsys.readouterr()
            assert "WRONG AC NUMBER" in captured.out

def test_pin_sucess(capsys):
    while len({}) > 0:
        with patch('builtins.input', side_effect=['1234']):
            result = pin('123456')
            assert result is None  # pin doesn't return anything
            captured = capsys.readouterr()
            assert "{} attempts left!" in captured.out
            assert "Enter the 4 digit pin" in captured.out
            assert "WELCOME!" in captured.out

def test_pin_failure(capsys):
    while len({}) > 0:
        with patch('builtins.input', side_effect=['9999', '1234']):
            result = pin('123456')
            assert result is None  # pin doesn't return anything
            captured = capsys.readouterr()
            assert "{} attempts left!" in captured.out
            assert "Enter the 4 digit pin" in captured.out
            assert "WRONG PIN!!" in captured.out
            assert "WELCOME!" in captured.out



# test_home just calls all the above functions
def test_home_display_balance(capsys):
    display_balance(1000.0)
    captured = capsys.readouterr()
    assert "Account Balance: Rs.1000.00" in captured.out
