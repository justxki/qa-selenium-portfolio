import pytest

from pages.bank import Bank

@pytest.mark.bank
def test_bank_init(bank):
    assert bank.balance == 0

@pytest.mark.bank
def test_bank_deposit(bank):
    bank.deposit(500)
    assert bank.balance == 500

@pytest.mark.bank
def test_bank_double_deposit(bank):
    bank.deposit(500)
    bank.deposit(900)
    assert bank.balance == 1400

@pytest.mark.bank
def test_bank_withdraw(bank):
    bank.deposit(500)
    bank.withdraw(200)
    assert bank.balance == 300

@pytest.mark.bank
def test_bank_withdraw_exact_balance(bank):
    bank.deposit(500)
    bank.withdraw(500)
    assert bank.balance == 0

@pytest.mark.bank
def test_bank_withdraw_over(bank):
    bank.deposit(500)
    with pytest.raises(ValueError):
        bank.withdraw(700)
###################################
def test_cant_withdraw_0(bank):
    with pytest.raises(ValueError):
      bank.withdraw(0)

def test_cant_deposit_0(bank):
    with pytest.raises(ValueError):
        bank.deposit(0)

def test_cant_withdraw_neg(bank):
    with pytest.raises(ValueError):
      bank.withdraw(-1)

def test_cant_deposit_neg(bank):
    with pytest.raises(ValueError):
      bank.deposit(-1)
###################################
cases = [
    ("withdraw", 0),
    ("deposit", 0),
    ("withdraw", -1),
    ("deposit", -1),
]

@pytest.mark.bank
@pytest.mark.parametrize("method_name, bad_value", cases)
def test_reject_bad_amounts(bank, method_name, bad_value):
    method = getattr(bank, method_name)
    with pytest.raises(ValueError):
        method(bad_value)

