#strings practice
name="sampath kayithi"
print(name[-1])

print(name.upper())
print(name.split())
print(name.startswith("s"))
print(name.endswith("h"))
#Problem:
'''
You are given a string sentence . Print the characters at even indices.
Example:
sentence = "Python is amazing"
# Output: "Pto saaig"
'''
sentence = "Python is amazing"
print(f"output is {sentence[::2]}")

#Problem:
'''
You are given a string s . Replace all spaces in the string with underscores ( _ )
and print the modified string.
Example:
s = "Python is fun and powerful"
# Output: "Python_is_fun_and_powerful"

'''
s = "Python is fun and powerful"
s1=s.replace(" ","_")
print(s1)
#Problem:
'''
You are given a string s . Check if the string contains only digits.
Example:
s = "1a345"
'''
s = "12345"
if s.isdigit():
    print(f"s is containing digits")
else:
    print(f"s is not contaning digits")

#Problem:
'''
You are given a string s . Print the string in reverse order.
Example:
Quiz Questions: 3
s = "Python is amazing"
# Output: "gnizama si nohtyP

'''
s = "Python is amazing"
s1=s[::-1]
print(s1)
#Problem:
'''
You are given a string s . Capitalize the first letter of each word in the string
and print the modified string.
Example:
s = "python programming is fun"
# Output: "Python Programming Is Fun"
'''
empty_list=[]
s = "python programming is fun"
words=s.split(" ")
for i in words:
    j=i.capitalize()
    empty_list.append(j)
print(empty_list)

    



