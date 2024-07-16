
from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sarah = BankAccount(10000, "Sarah")
Jim = InterestRewardsAcct(1000, "Jim")

Jim.getBalance()

Jim.deposit(100)

Jim.transfer(100, Dave)


Dave.withdraw(10)

Brianna = SavingsAccount(1000, "Brianna")

Brianna.getBalance()

Brianna.deposit(100)

Brianna.transfer(100, Sarah)

Sarah.getBalance()