#Task 1:
'''
Write Python code to reverse the order of elements in the given list my_list .
Print the reversed list.
my_list = [10, 20, 30, 40, 50, 11]
# Your code here
# Output should be: [11,50,40,30,20,10]

'''
# my_list = [10, 20, 30, 40, 50, 11]
# print(f"Reverse order of elements is: {my_list[::-1]}")

#Task 2:
'''
Common Elements:
Given two lists list1 and list2 , find and print the common elements between
them.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
# Your code here
Quiz Questions: 3
# Output should be: [4, 5]
'''
# my_list=[]
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# for i in list1:
#     for j in list2:
#         if i==j:
#             my_list.append(i)
# print(my_list)

#Task 3:
'''
Unique Elements:
Create a new list unique_list containing only the unique elements from the
given list original_list . Print the unique list.
original_list = [1, 2, 2, 3, 4, 4, 5]
# Your code here
# Output should be: [1, 2, 3, 4, 5]

'''
# unique_list=[]
# original_list = [1, 2, 2, 3, 4, 4, 5]
# for i in original_list:
#     if i not in unique_list:
#         unique_list.append(i)
# print(unique_list)

#Task 4:
'''
Remove Duplicates:

Remove duplicate elements from the given list duplicated_list and print the list
without duplicates while preserving the order.
duplicated_list = [1, 2, 2, 3, 4, 4, 5]
# Your code here
# Output should be: [1, 2, 3, 4, 5]
'''
# dup_list=[]
# duplicated_list = [1, 2, 2, 3, 4, 4, 5]
# for i in duplicated_list:
#     if duplicated_list.count(i)>1 and i not in dup_list:
#         dup_list.append(i)
# print(dup_list)

#Exercise 1: List Concatenation
'''
Write a Python script that concatenates two lists and prints the result.

'''
# lst1=[3,5,6,7,8,93,45]
# lst2=[34,45,56,46,78]
# conc_list=lst1 + lst2
# print(conc_list)
#Exercise 2: List Repetition
'''
Write a Python script that repeats a list three times and prints the result.
'''
# sample_lst=[1,2,3,4,5,6]
# rep_list=[sample_lst]*3
# print(rep_list)

#Exercise 3: List Removal
'''
Write a Python script that removes the elements at even indices from a list.
'''
temp_list1 = [1,2,3,4,5,6,10,11,23,34]
result = temp_list1[1::2]
print(result)

#Exercise 4: List Insertion
'''
Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of
a list

'''

lst3=[3,5,6,7,8,93,45]
lst3.insert(0,10)
lst3.insert(1,11)
lst3.insert(2,12)
print(lst3)

#List comprehensions
'''
1. Square Numbers: Create a list of squares of numbers from 1 to 10.
'''
#syntax
#[experssion for i in iterable if cond]
result=[i*i for i in range(1,11)]
print(result)

'''
2. Even Numbers: Generate a list of even numbers from 1 to 20.
'''
print([i for i in range(1,21) if i %2==0])

'''
3. Words Lengths: Given a list of words, create a list containing the lengths of
each word.
words = ["apple", "banana", "cherry", "date"]
'''
new_list=[]
words = ["apple", "banana", "cherry", "date"]
for i in words:
    j=len(i)
    new_list.append(j)
print(new_list)

















#Write a Python script that removes the elements at even indices from a list.
















    





