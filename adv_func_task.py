# Advance function practice
'''
Write a Python function 
square_all(numbers) that takes a list of numbers as input 
and returns a new list containing the square of each number in the input list. 
Use the 
map() function with a lambda function to implement this
'''
lst=[2,3,4,5,6,7,9,5,0]
result= map(lambda a:a**2,lst)
print(list(result))
#or
print(list(map(lambda a:a**2,lst)))

'''
Write a Python function 
filter_positive(numbers) that takes a list of numbers as 
input and returns a new list containing only the positive numbers from the 
input list. Use the 
filter() function with a lambda function to implement this.
'''
lst1=[-1,-2,-3,-4,-5,0,1,2,3,4,5]
result=filter(lambda a:a>=0,lst1)
print(list(result))

'''
Write a Python function 
calculate_factorial(n) that calculates the factorial of a 
given number n. Use the 
reduce() function with an appropriate lambda 
function to implement this
'''
# n=int(input("Enter a number:"))
# from functools import reduce
# result=reduce(lambda a,b:a*b,range(1,n+1))
# print(result)

'''
Write a Python function 
count_vowels(string) that takes a string as input and 
returns the count of vowels (a, e, i, o, u) in the input string. Use the 
reduce() 
function with an appropriate lambda function to implement this
'''

# name=input("Enter the string:")
# from functools import reduce
# result=reduce(lambda )
lst="aeiouAEIOU"
name=input("Enter the string")
from functools import reduce
result= reduce(lambda a,b:a+1 if b in lst else a )
print(result)











