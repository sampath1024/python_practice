# Creating an ATM project
#Author: Sampath K
actions='''
Withdrawl
Deposit
Pin change
Balance Enquiry
'''
Amount= 0
oldpin=1234
Account_number= 12345678

#actions=["Withdrawl","Deposit","Pin change","balance enquiry"]
actions=[1,2,3,4,5]
def withdrawl():
   global Amount
   wa=float(input("Enter the amount to withdrawl:"))
   if wa<=Amount:
    print("Processing your withdrwal\tPlease collect the cash")
    Amount-=wa
    print(f"You have withdrawed an amount of {wa} and remaining balance is {Amount}")
   else:
    print("Insufficient funds in your account")

def deposit():
    global Amount
    da=float(input("Enter the amount to be deposited:"))
    if da<=0:
      print("Please enter positive numbers")
      return
    Amount+=da
    print(f"You have deposited {da} and Total balance is {Amount}")

def pin_change():
    global oldpin
    old= int(input("Enter the current pin:"))
    if old != oldpin:
      print("Wrong pin")
      return
    new=int(input("Enter the new pin:"))
    oldpin =new
    print("PIN changed")

def balance_enquiry():
    global Amount
    acc=int(input("Please enter the account number:"))
    pin=int(input("Please enter the pin to verify:"))
    if acc == Account_number and pin == oldpin:
     print(f"You account balance is fetched succesfully {Amount}")
    else:
     print("Invalid details, Kindly enter valid inputs")
while True:
    print("\nATM Menu:")
    print("1. Withdrwal")
    print("2. Deposit")
    print("3. pin_change")
    print("4. balance_enquiry")
    print("5. Exit")
    choice = int(input("Enter your choice (1-5): "))
    if choice == actions[0]:
      withdrawl()
    elif choice == actions[1]:
      deposit()
    elif choice== actions[2]:
      pin_change()
    elif choice== actions[3]:
      balance_enquiry()
    elif choice == actions[4]:
      break
    else:
      print("Invalid entry")



