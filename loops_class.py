#for loop ---> to iterate over a sequence
#syntax
# for variable in sequence:
#     #statement 1
#     #statement 2
# list_1 = ["maheswari","kumar","charan","ganesh","ram"]
# for i in list_1:
#     print(i)


# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:
#     print(f"{fruit} stock received")


# employee_data = ["ganesh","naveen","vijay","venu","pranaya"]
# for i in employee_data:
#     print(f"{i} salary 5 % hike given")

# range(stop)
# range(start, stop)
# range(start, stop, step)
# for i in range(10):
#     print(i)

# for i in range(2,11):
#     print(i)


# for i in range(1,11,2):
#     print(i)


# for i in range(499,1001):
#     print(i)


#multiplication of 2 Table
# for i in range(1,11):
#     print(f"2 X {i} = {i*2}")




# for i in range(1,21):
#     print(f"17 X {i} = {i*17}")



#syntax
#nested for loop
# for i in sequence:
#     for j in sequence:

# for i in range(5):#outer loop
#     for j in range(5):#inner loop
#         print(i,j)


# for i in range(1,11):
#     for j in range(1,21):
#         print(f"{i} x {j} ={i*j}")
#     print()


# prices = [99,100,200,101]
# for i in prices:
#     print(i+2)




#syntax
# while condition:True
#     #block of code

# age = 18
# while age>=18:#True
#     print("you are eligible to vote")
#     break


# count = 0
# while count<3:
#     print(count)
#     count +=1

# while True:
#     user_name = input("enter username: ")
#     password = input("enter the password: ")
#     if user_name == "ram" and password == "1234":
#         print("login success")
#         break
#     else:
#         print("invalid credentials")


# while condition:
#     while condition:

# age = 50
# while age>=35:#outer while loop
#     print("this is outer while loop")
#     age -= 1
#     print(age)
#     while age>=35:#inner while loop
#         print("this is inner while loop")
#         break

# for i in range(0,10,1):
#     print(i)

# outer = 0
# while outer < 3:
#     inner = 0
#     while inner < 2:
#         print(outer, inner)
#         inner += 1
#     outer += 1


# while True:
#     print("hi")


# Write a program to display all prime numbers within a range
# first_number = int(input("please enter first number in range: "))
# last_number = int(input("please enter last number in range: "))

# for num in range(first_number, last_number +1):
#     if num > 0:
#         for i in range(2, num): 
#             if num % i == 0:
#                 break 
#         else:
#             print(num)

# for i in range(2,3):
#     print(i)

# diplay prime numbers between given numbers particular range
# for num in range(2,101):
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         print(num)











# count = 0
# while count<5:
#     count +=1 
#     print(count)


