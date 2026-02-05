#Python program that prints your name.
print("sampath")
'''
Python script with both single-line and multi-line comments 
explaining the purpose of the script
'''
#my_name=input("enter your name")
#print(my_name)

"""
above script use input function, with this user can give input in the console
"""
# list containing three different data types.
record=["sampath",29,164.5]
print(record)
print(type(record))
#set containing employee idʼs.#
emp_data={3455,3465,9875,9087}
print(emp_data)
print(type(emp_data))
#concatination
name="sampath"
sur_name="kayithi"
full_name= name + sur_name
print(full_name)
#repetation of string
brand="toyota"
brand="maruti"
brand="tata"
print(brand)
#using keyword as a variable
#for= "sampath"
#break= "shekar"
#print(for)
#print(break)
"""
here is the error it is showing, if we use built in keywords as variables
Error:
SyntaxError: invalid syntax

D:\python\programs>C:/Users/sampa/AppData/Local/Microsoft/WindowsApps/python3.12.exe d:/python/programs/fundamentals_1-1.py

  File "d:\python\programs\fundamentals_1-1.py", line 32
    for= "sampath"
       ^
SyntaxError: invalid syntax
"""

#Declare two variables, one storing an integer and the other a string. 
#Print their values
citizen_name="ramu"
citizen_id="12345678"
print(citizen_name)
print(citizen_id)

#type conversions 
# float to string
percentile= 98.7
print(type(percentile))
percentage=int(percentile)
print(percentage)
print(type(percentage))
#int to string
score=95
print(type(score))
score_update=str(score)
print(score_update)
print(type(score_update))
#input function
#age=input("enter your age")
#print(age)
###############################################PART-2##########################################################
###############################################PART-2##########################################################

#pattern printing
print("###############")
print("#############")
print("############")
print("###########")
print("##########")
print("#########")
print("########")
print("#######")
print("######")

#Comments

employee_names=["soujanya","shekar","rajkumar","santhosh"] # employee details are mentioned in lists
employee_id=(10124466,1456677,55663663,53636636) # id's are unique so mentioned in tuples
data={
    "soujanya":10124466,
    "shekar":1456677,
    "rajkumar":55663663,
    "santhosh":536366
}   # organized the above data in a dictionary for easy readibility
print(data) 

# dictionary practice

book_store={
      "tile": "kadali",
      "author": "satya",
      "publication_year":2010
}

#string_operations
data=35
accurate_data=float(data)
print(accurate_data)
print(type(accurate_data))

#concatination
# name=input("enter name")
# sur_name=input("enter sur name")
# full_name= name + sur_name
# print(full_name)


#conversion
# input function by default takes string, so if we give floating point as input it is showing literal error
# so i am converting to float firts

# basic rule ##INPUT FUNCTION BE DEFAULT TAKES INPUT AS STRING#
# age=float(input("enter the age"))
# conv_age= int(age)
# newage= conv_age + 5
# print(newage)

# calculator programme
value_1=int(input("enter the first number"))
value_2=int(input("enter the second number"))
addition= value_1 + value_2
subtraction= value_1 - value_2
print(addition)
print(subtraction)






