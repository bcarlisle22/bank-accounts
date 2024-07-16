# use code runner to change where output goes (terminal/output) turn "run in terminal" on/off

# dont forget new line uses "\" not "/" 
class BalanceException(Exception): #
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print("\n")
        print(f"\nAccount '{self.name}'created. Balance = ${self.balance:,.2f}") 
        print("\n")
        #ERROR:(line 5)invalid syntax error SOLUTION: when running code in oop_project file, make sure to select "run python file"
        
    def getBalance(self):
        print("\n")
        print(f"\nAccount '{self.name}'created. Balance = ${self.balance:,.2f}")
        print("\n")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\n")
        print("Deposited")
        print("\n")
        print(f'{self.balance:,.2f}')
        print("\n")
    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\n Sorry, account '{self.name}' only has a balance of ${self.balance:,.2f}"
            )
    def withdraw(self, amount):  
        try:                                              #
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\n")
            print("\nWithdraw complete.")
            print("\n")
            self.getBalance()
        except BalanceException as error:
            print("\n")
            print(f"\n Withdraw interrupted: {error} ")  #
            print("\n")
            
    def transfer(self,amount, account):
        try:
            print("\n")
            print('\n****************\n\nBeginning Tranfer ')
            print("\n")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\n")
            print('\nTransfer Complete!\n\n***************')
            print("\n")
        except BalanceException as error:
            print("\n")
            print(f'\n Transfer interrupted. {error}')
            print("\n")

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()


class SavingsAccount(InterestRewardsAcct):
    def __init__ (self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')
