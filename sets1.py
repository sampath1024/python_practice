#sets_practice
my_set = {1, 2, 3, 4, 5}
print(len(my_set))
my_set.add(6)
print(my_set)
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2)) # combing elements by ignoring common elements
print(set1.intersection(set2)) # common elements
#Task 1: Set Intersection
#Task 2: Set Union
#Task 3: Set Difference
#Task 4: Set Symmetric Difference
'''
Write Python code to find and print the intersection of the following two sets:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# Your code here
# Output should be: {4, 5}

'''
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.intersection(set2)) # common elements
print(set1.union(set2)) # combing elements by ignoring common elements
print(set1.difference(set2)) 
print(set1.symmetric_difference(set2))
#Task 5: Set Membership Test
'''
Write Python code to check if the element 3 is present in the set 
my_set = {1, 2, 3, 4, 5}
# Your code here
# Output should be: True
'''
my_set = {1, 2, 3, 4, 5}
if 3 in my_set:
    print("True")
#Exercise 1: Set Intersection
'''
Write a Python script that finds and prints the intersection of two sets.
'''
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.intersection(set2))




