#ATM
class ATM():
    def __init__(self,bankname,branch,Amount=0):
        self.bankname=bankname
        self.branch=branch
        self.Amount=Amount
    def deposist(self,da):
        if da<=0:
            print("Amount must be greater than zero")
        else:
            self.Amount+=da
            print(f"{da} amount is being deposited")
        
    def withdraw(self,wd):
        if wd<=0:
            print("Amount must be greater than zero")
        else:
            self.Amount-=wd
            print(f"{wd} withdrawn")
    
    def balance(self,AN=2345678,pin=1234):
        AN1=int(input("Enter the account number:"))
        pin1=int(input("Enter the pin to verify:"))
        if AN == AN1 and  pin == pin1:
            print(f"balance is fetched {self.Amount}")
        else:
            print("Invalid details.")
atm = ATM("nachupally", "jntu", 5000)
class ATM2(ATM):
    def ministatment(self):
        pass
while True:
    print("\n ATM menu")
    print("1, withdrwl")
    print("2, deposit")
    print("3, balance")
    print("4, Exit")

    choice=int(input("Enter your choice:"))
    if choice == 1:
        atm.withdraw(int(input("Enter the amount for withdrawl:")))
    elif choice == 2:
        atm.deposist(int(input("Enter the amount for deposit:")))
    elif choice == 3:
        atm.balance()
    elif choice == 4:
        print("Thank you for using ATM...")
        break


