import pytest

@pytest.fixture
def dummy_user():
    return {"username": "standard_user", "password": "secret_sauce"}

def test_fixture_works(dummy_user):
    assert dummy_user["username"] == "standard_user"


def upping_word(text):
    return text.upper()

def test_numbs_upper():
    with pytest.raises(AttributeError) as e:
        upping_word(123)

    assert "int" in str(e.value)

def divide_numbers(a, b):
    return a / b

def test_div_zero():
    with pytest.raises(ZeroDivisionError) as e:
        a = 5
        b = 0
        divide_numbers(a, b)

    assert "zero" in str(e.value)

def test_numbs_upper_false_pass():
    with pytest.raises(Exception): # ❌ Using the base Exception class
        upping2_word() # But forgetting to define what 'upping_word' is or passing wrong arguments