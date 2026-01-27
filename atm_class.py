class ATM():
    def __init__(self,da,wa,Amount):
        self.da=da
        self.wa=wa
        self.Amount=Amount
    def withdrawl(self):
      #global Amount
      #wa=float(input("Enter the amount to withdrawl:"))
      if self.wa<=self.Amount:
       print("Processing your withdrwal\tPlease collect the cash")
       self.Amount-=self.wa
       print(f"You have withdrawed an amount of {self.wa} and remaining balance is {self.Amount}")
      else:
       print("Insufficient funds in your account")
    def deposit(self):
      #global Amount
      #da=float(input("Enter the amount to be deposited:"))
      if self.da<=0:
       #print("Please enter positive numbers")
       return
      self.Amount+=self.da
      print(f"You have deposited {self.da} and Total balance is {self.Amount}")
    # def pin_change(self):
    #  global oldpin
    #  old= int(input("Enter the current pin:"))
    #  if old != oldpin:
    #   print("Wrong pin")
    #   return
    # new=int(input("Enter the new pin:"))
    # oldpin =new
    # print("PIN changed")

obj=ATM("1500","1000",0)
#obj.withdrawl()
obj.deposit()


