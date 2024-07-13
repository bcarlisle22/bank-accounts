#  dont forget: line breaks are front slash not backslash lol 

class customerAccounts: # class
    def __init__(self, customerBalance, customerName):
        self.balance = customerBalance
        self.name = customerName
        print(f"\n Account {self.name} created \n Account Balance: ${self.balance:.2f} \n") 
        # reminder: f strings (^) are good for when you need to use string 
        # literals in your output - good for formatting

        def getBalance(self): # method
            print(f"\n Account '{self.name}' balance = ${self.balance:.2f} ")

