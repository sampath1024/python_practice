#operators practice
'''
Create a program that takes user input for their name and age.
Use formatted strings (f-strings) to print a message welcoming the user and
stating their age.
'''
user_name=input("enter the name:")
user_age=input("Enter the age:")
print(f"Welcome Mr {user_name} and his age is {user_age}")

'''
Create a list called numbers that contains integers from 1 to 10.
Check if the number 5 is in the list.
Check if the number 15 is not in the list.
'''
real_number=[1,2,3,4,5,6,7,8,9,10]
print(5 in real_number)  # Returns the boolean value true 
print(15 not in real_number) # Returns the boolean value true

#Exercise1
'''
Write a Python program to calculate the area of a rectangle using the given
formula: area = length * width . Take the values of length and width as inputs from
the user.
'''
length=int(input("Enter the lenth of the rectangle:"))
width=int(input("Enter the width of the rectangle:"))
print(f"Area of the rectangle having length of {length} and width of {width} is {length * width}")

#Exercise2
'''
Write a Python program to demonstrate incrementing and decrementing a variable
'''
value= 10
value+=5
print(f"{10} is being incremented by {5} with help of compounding assignment operators")
value1=50
value1-=5
print(value1)

value2=20
value2*=2
print(value2)

value3=30
value3/=10
print(value3)

value4=20
value4//=6
print(value4)

#Exercise 3
'''
Write a Python program to convert temperature from Celsius to Fahrenheit. The
formula for conversion is: F = (C * 9/5) + 32 . Take the temperature in Celsius as
input from the user
'''
temp_cels=int(input("Enter the temperature in celcius"))
temp_far=(temp_cels * (9/5) + 32)
print(temp_far)

#Exercise4
'''
Write a Python program to calculate the simple interest given the principal
amount, rate, and time (in years).
'''

amount=int(input("Enter the principle amount:"))
rate=int(input("Enter the rate value:"))
time=int(input("Enter the time in years"))
print(f"Intrest levied on {amount}/- for the period of {time} year at a rate of {rate}% is {(amount * time * rate)/100}/-")

#Exercise 5
'''
Write a Python program to concatenate two strings and display the result. The
strings should be taken as input from the user.
'''
greeting=input("Enter the greet:")
name=input("Enter the name of the person:")
result=greeting + name
print(result)

#Exercice 6
'''
Write a Python program to convert a distance from kilometers to miles.
'''
dist_km=int(input("Enter the distance in km's:"))
dist_mile=dist_km * 0.621371
print(dist_mile)
