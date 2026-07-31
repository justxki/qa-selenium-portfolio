class Bank:
    def __init__(self):
        self._balance = 0

# Okay how do i decide when to put _? for banking, balance should always start at 0 and not be touched by other devs? Not my circus tho i guess lmfao

#Okay see same with the methods like how do i decide to put _ also which to use? setter, property, add? WHICH?!

#okay okay you WONT want any code to affect balance. window to see in, not to touch.
    @property
    def balance(self):
        return self._balance

# THE BUTTON to change the number on the paper.
    def deposit(self, deposit_amount):
        if deposit_amount <= 0:
            raise ValueError("Can't deposit negative money brokie.")
        self._balance += deposit_amount

# ANOTHER BUTTON to change the number on the paper.
    def withdraw(self, withdraw_amount):
        if withdraw_amount <= 0:
            raise ValueError("You're not withdrawing anything brokie.")
        if withdraw_amount > self._balance:
            raise ValueError("Can't withdraw more than balance amount brokie.")
        self._balance -= withdraw_amount


#bank = Bank()
#print(bank._balance)
#bank.deposit(500)
#print(bank._balance)
#bank.withdraw(0)
#bank.deposit(0)
#bank.withdraw(5000)

