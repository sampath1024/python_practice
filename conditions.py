#Vowel checker
'''
Write a Python program that takes a character as input and checks whether
it is a vowel or not. 
'''
value="aeiouAEIOU"
value_1=input("Enter the characters")
if value_1 in value:
    print("It it a vowel")
else:
    print("not a vowel")

#Age Group Classification
'''
Write a program that takes an age as input and classifies the person into
one of the following age groups
'''
age=int(input("Enter the age:"))
if age>=0 and age<=12:
    print("You are a child")
elif age>=13 and age<=17:
    print("you are a teenager")
elif age>=18 and age<=64:
    print("you are an adult")
elif age>=65:
    print("you are senior")
else:
    print("invalid values")

#Number Classifier:
'''
Write a program that takes an integer as input and classifies it as positive,
negative, or zero.
'''
num=int(input("Enter the number:"))
if num>0:
    print(f"given {num} is positve")
elif num<0:
    print(f"given {num} is negative")
else:
    print(f"given {num} is zero")

#Leap Year Checker:
'''
Create a program that checks whether a given year is a leap year or not. A
leap year is divisible by 4, but not by 100 unless it is divisible by 400.
'''
year=int(input("Enter the year to check:"))
if year%400==0:
    print(f"Given {year} is leap year")
elif year%4==0 and year%100!=0:
    print(f"Given {year} is leap year")
else:
    print(f"given {year} is not a leap year")

#calculator
'''
Build a simple calculator program that takes two numbers and an operator
(+, -, *, /) as input and performs the corresponding operation.
'''
num_1=float(input("Enter the first number:"))
num_2=float(input("Enter the second number:"))
ops=input("Enter the operation to perform:")
#=input("Enter the operation:")
if ops=="+":
    print("Result:", num_1 + num_2)
elif ops=='-':
    print("Result:",num_1 - num_2)
elif ops=='*':
    print("Result:",num_1 * num_2)
elif ops=='/':
     if num_2==0:
        print("dividinig a number by zero result infinite")
     else:
        print("Result:", num_1/num_2)
else:
    print("invalid operation")




#short hand if
'''
Rewrite the following code using the short-hand
if statement:
#############
x = 8
if x % 2 == 0: result = "Even"
else: result = "Odd"
'''
x=9
print(f"even")if x%2==0 else print(f"odd")

#Discount_calculator
'''
Create a program that calculates the final price after applying a discount.
The program should take the original price and the discount percentage as
input.
'''
org_price=int(input("Enter the oroginal price:"))
discount_per=int(input("Enter the discount percentage:"))
final_price= org_price-(org_price*discount_per/100)
print(f"After applying {discount_per}% discount final price will be {final_price}")

#BMI Calculator:
'''
Write a program that calculates the Body Mass Index (BMI) using the
formula: BMI = weight (kg) / (height (m))^2. The program should take
weight and height as input.
'''
w=float(input("Enter the weight:"))
h=float(input("Enter the height:"))
if w<=0 or h<=0:
    print("Weight and height must be positive numbers")
else:
    bmi=(w/ ((h/100) ** 2))
    print(f"BMI value of person with {w} and {h} is {bmi}")
    








