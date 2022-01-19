class bank:
    def __init__(self):
        self.balance=0
        name=input("Enter the name of account holder : ")
        acno=int(input("Enter the account no : "))
    
        print ("\n---The account is created---")
        print("\nName of Account Holder : ",name)
        print("\nAccount no : ",acno)
        
    def deposit(self):
        amount=int(input("\nEnter the amount to deposit : "))
        self.balance+=amount
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn : "))

        if (self.balance>=amount):
            self.balance-=amount
            print("\nYou Withdraw:", amount)
        else:
            print("\nInsufficient balance!!!")
            
    def display(self):
        print("\nAvailable Balance : ",self.balance)
        
b=bank()
b.deposit()
b.withdraw()
b.display()