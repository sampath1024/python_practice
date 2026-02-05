#Exercise 1: Sum of Squares
'''
Write a Python program that calculates and prints the sum of the squares of
numbers from 1 to 5 using a
for loop
'''
# sum=0
# for i in range(1,6):
#     print(f"sum of the squares for given range is {(i*i)+sum}")
#     sum+=i

#Exercise 2: Countdown
'''
Write a Python program that uses a
while loop to print a countdown from 5 to 1.
'''
# count=5
# while count>0:
#     print(count)
#     count-=1
#Exercise 3: Multiplication Table with Nested For Loop
'''
Write a Python program to print the multiplication table for a user-specified
number using a nested for loop
'''
number=int(input("Enter the number:"))
for i in range(1,number+1):
   for j in range(1,11):
      print(f"{i} X {j} = {i*j}")

#Exercise 4:
'''
Write a Python program that uses a "for" loop to find the sum of all even
numbers between 0 and 10 (inclusive).
'''
# sum=0
# for i in range(0,11):
#     if i%2==0 and i!=0:
#      sum += i
# print(sum)





#Exercise 5:
'''
Calculate the sum of all numbers from 1 to a given number
'''
# n = int(input("Enter a number: "))

# if n < 1:
#     print("Invalid input")
# else:
#     total = 0
#     for i in range(1, n + 1):
#         print(i)
#         total += i
#     print("Sum:", total)


#Exercise 6:
'''
Display numbers from a list using loop
'''
# rankings=[1,5,4,7,8,0,3]
# for i in rankings:
#     print(i)

#==========================================================================================================#
#Exercise 7:
'''
Display numbers from -10 to -1 using for loop
'''
# for i in range(-10,0):
#     print(i)
#===========================================================================================================#   
#Exercise 8:
'''
Write a Python program to print the cube of all numbers from 1 to a given
number
'''
# given_num=int(input("Enter a number"))
# for i in range(1,given_num+1):
#     print(f"cube of all numbers in range is {i**3}")


