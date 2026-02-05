# input function practice # 
"""
Below code will concatinate the entered
numbers, because by default input function takes
input as string datatype
"""
empid_1= input("enter the number:")
empid_2= input("enter the number:")
sum = empid_1 + empid_2
print(sum)

#fixed version, which adds the numbers based on input
empid_1= int(input("enter the number:"))
empid_2= int(input("enter the number:"))
sum = empid_1 + empid_2
print(sum)