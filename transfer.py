#Problem 1: Using break in a While Loop
'''
Write a Python program that takes a list of numbers as input numbers = [25, 30,
20, 40, 15, 25] and prints the sum of the numbers. However, if the sum exceeds
100, stop adding numbers and print "Sum exceeded 100".

'''
# sum=0
# data= [25, 30,20, 40, 15, 25]
# for i in data:
#     sum+=i
#     if sum>=100:
#         break
# print(f"Sum exceeded 100 and value is:{sum}")
# print(f"Last iteration value:{i}")

#Problem 2: Using continue in a For Loop
'''
Write a Python script that uses a for loop to iterate through numbers from 1 to
600. Print only the odd numbers, skipping the even ones using the continue
statement.
'''
# for i in range(1,601):
#     if i%2==0:
#         continue
#     print(i)
#Problem 3: Using pass in Conditional Statements
'''
Write a Python script that checks if a number is even or odd. If the number is
even, print "Even"; if odd, do nothing (use the pass statement).

'''
# value=int(input("Enter a number to check:"))
# if value%2==0:
#     print(f"{value} is even")
# elif value%2!=0:
#     pass

#Problem 4: Combining Transfer Statements
'''
Write a Python script that iterates through a list of words. If the word is "break,"
exit the loop using the break statement. If the word is "skip," skip the rest of the
code for the current iteration using the continue statement. For any other word,
print the word.

'''

words=["break","skip","sampath","shekar"]
for i in words:
    if i=="break":
        #print("breaking the loop")
        break
    elif i=="skip":
        #print("contiuing the loop by skipping skip word")
        continue
    else:
        print("word")
#print(i)

    





