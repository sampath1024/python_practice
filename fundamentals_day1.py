# this script is to practice comments
print('my name is sampath')
'''
Comments are of two types
single line and multi-line comments
to give short name for a programme we use 
single line and for the detailed info
multi-line comments comes handy
'''
"""
We can use double-quotes as well,
words or sentences enclosed in single or double quotes 
will not be executed
"""
# two variables, one storing an integer and the other a string. Print
#their values.
#varibles
#syntax: varibale=value
student_name="sampath" #string declaration
student_id=2345 # integer declaration
print(student_name)
print(student_id)
#program that prints a pattern using multiple print statements.
print("************")
print("***********")
print("********")
print("******")
print("**********")
print("************")
print("*************")

#Python script for a simple task and add comments to explain each step.
value_1= 100 # input 1
value_2= 200 # input 2
result = value_1 + value_2 # adding both
print(result) # will display the output to screen

#Create variables of different data types(int,float,str) and print their values.
student_name="sampath" #string declaration
student_id=234 # integer declaration
student_height=164.5 #float declaration
print(student_name)
print(student_id)
print(student_height)

#Determine the data type of a variable.
print(type(student_name))
print(type(student_id))
print(type(student_height))
#memory address
employee_id=10
person_age=25
print(id(employee_id))
print(id(person_age))

#type_conversion
age="35"
print(type(age))  # before
int_conv=int(age)
print(int_conv)    
print(type(int_conv)) # after

#concatination
empid_1= input("enter the number:")
empid_2= input("enter the number:")
sum = empid_1 + empid_2
print(sum)


#self practice

#type_conversion
#int to float
number=float(student_id)
print(number)
print(type(number))
#int to string
name=str(student_id)
print(name)
print(type(name))
#string to integer # invalid one
#new_integer=int(student_name)
#print(new_integer)
#print(type(new_integer))



#fixed version, which adds the numbers based on input
empid_1= int(input("enter the number:"))
empid_2= int(input("enter the number:"))
sum = empid_1 + empid_2
print(sum)












