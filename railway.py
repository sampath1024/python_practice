import random
import datetime
import time
# accounts={
#     "sampath":12345,
#     "shekar":12345,
#     "soujanya":45678,
# }
accounts={}
while True:
    options='''
      1. Exit
      2. Account creation
      3. Login
 '''
    print(options)
    choice=int(input("Enter your choice of action:"))
    if choice ==1:
        break
    elif choice ==2:
          user=input("Enter a username to create:")
          pwd=int(input("Enter the password:"))
          accounts[user]=pwd
          print(accounts)
    elif choice ==3:
         login=input("Enter the login name:")
         login_pwd=int(input("Enter the password:"))
         print(login)
         print(login_pwd)
         #rint(accounts.keys)
         if login in accounts and login_pwd==accounts[login]:
              print("Authentication success:")
              passenger_list={}
              while True:
                   train_details=[]
                   options='''
                   1. Exit
                   2. Train details
                   3. Booking
                    '''
                   print(options)
                   val=int(input("Enter your option:"))
                   if val == 1:
                        break
                   elif val == 2:
                        print("Current available trains:")
                        Trains='''
                      1:Train Number: 12345
                        Hyd to Bangalore

                      2:Train Number: 67890
                        Hyd to Chennai

                      3:Train Number: 56789
                        Hyd to Mumbai
                        
'''
                        print(Trains)
                        Trains_det=[{"Train No": 12345,
                                   "From": "Hyd",
                                   "To" : "Bangalore"
                        },
                        {
                                   "Train No": 67890,
                                   "From" : "Hyd",
                                   "To" : "Chennai",
                        },
                         {
                                   "Train No": 56789,
                                   "From" : "Hyd",
                                   "To" : "Mumbai"

                         }    

                        ]
                   elif val ==3:
                        print(Trains)
                        train_choice=int(input("Choose the train you want to book:"))
                        if train_choice == 1:
                             print(f"You have choosen {Trains_det[0]}")
                             choosen_train=Trains_det[0]
                        elif train_choice ==2:
                             print(f"you have choosen {Trains_det[1]}")
                             choosen_train=Trains_det[1]
                        elif train_choice ==3:
                             choosen_train=Trains_det[2]
                        price_per_ticket=500
                        while True:
                         artifacts='''
                            1: Exit
                            2: Enter passenger details
                         
'''
                         print(artifacts)
                         art=int(input("choose a artifact:"))
                         if art == 1:
                              break
                         elif art ==2:

                              name=input("Enter the Name for booking:")
                              age=int(input("Enter the age:"))
                              passenger_list[name]=age
                              No_of_passengers=len(passenger_list.keys())
                              print("Calculating the ticket_fare:")
                              Tickt_fare=No_of_passengers * price_per_ticket
                              print("##########Booking Details#########")
                              for p in passenger_list.keys():
                               print(f"Name:{p}")
                               print(f"age:{age}")
                               print(f"Train details:{choosen_train}")
                               print(f"Fare:{Tickt_fare}")
         else:
              print("Exit")
              




                        
