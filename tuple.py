#tuple practice
print(all(()))
#Coding Exercise:
'''
Create a Tuple: Write a program that creates a tuple containing three 
elements: your name, your age, and your favorite color. Then print the
tuple
'''
detail=("ravi",39,"blue")
print(detail)

#Access Tuple Elements
'''
Write a program that creates a tuple containing the 
days of the week. Then, print the third element of the tuple
'''
days=("Mon","Tue","Wed","Thu","Fri","Sat")
print(days[2])

# Tuple Concatenation
'''
Write a program that creates two tuples, one 
containing odd numbers from 1 to 5 and another containing even numbers 
from 2 to 6. Concatenate these two tuples and print the result.
'''
odd=(1,3,5)
even=(2,4,6)
print(odd+even)

# Tuple Unpacking
'''
Write a program that defines a tuple containing the 
dimensions of a rectangle (length and width). Then, unpack this tuple into 
two variables and calculate the area of the rectangle.
'''
dimensions=(25,30)
length=dimensions[0]
width=dimensions[1]
print(f"Area of rectangle with {length} and {width} is {length * width}")

#Check if an Element Exists
'''
Write a program that checks if a given element 
exists in a tuple
'''
days=("Mon","Tue","Wed","Thu","Fri","Sat")
if "Mon" in days:
    print("True")



