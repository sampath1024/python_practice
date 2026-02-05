# #Types of error
# #ZeroDivisionError You tried to divide by zero. Python won’t “handle it magically”
# # num1=int(input("Enter a number:"))
# # num2=int(input("Enter second number:"))
# # try:
# #   result=num1/num2
# # except ZeroDivisionError as e:
# #   print(e)

# #TypeError--You’re using incompatible data types together.
# name="sampath"
# id=1234
# try:
#  print(name+id)
# except TypeError as e:
#  print(e)
# #ValueError --Correct type, wrong value.
# try:
#  int("abc")
# except ValueError as e:
#  print(e)
# #IndexError--You tried to access an index that doesn’t exist.
# lst=[1,2,3,4,5]
# try:
#   if lst[5] == 6:
#     print("6 exist")
#   else:
#     print("not exist")
# except IndexError as e:
#  print(e)
# #KeyError--You asked a dictionary for a key it doesn’t have.
# dict1={"Maths": 100,"Physics":90,"English":95}
# try:
#  a=dict1["social"]
#  print(a)
# except KeyError as e:
#  print(e)
# #NameError--Python has no idea what variable or function you’re talking about.
# #Why it happens: Typos, or using something before defining it.
# try:
#  print(sampath)
# except NameError as e:
#  print(e)
# #AttributeError-- You’re calling an attribute or method that doesn’t exist for that object.
# class sample():
#  def sample1(self):
#   print("sample1 block")
#  def sample2(self):
#   print("sample2 block")
# obj=sample()
# try:
#  obj.sample3
# except AttributeError as e:
#  print(e)

# #FileNotFoundError -- You tried to open a file that isn’t there.
# try:
#  file=open("new.txt","r")
#  file.close()
# except FileNotFoundError as e:
#  print(e)

# #ImportError / ModuleNotFoundError-- Python can’t find the module you’re importing.
# try:
#     import latest
#     import python
# except ImportError as e:
#  print(e)

# #RecursionError -- Your function called itself too many times.
# try: 
#  def fact(n):
#      return n * fact(n - 1)
#  fact(5)
# except RecursionError as e:
#  print(e)

#Multithreading
#Example without threads
# import time
# def task(name):
#     print(f"starting task {name}")
#     time.sleep(2)
#     print(f"finished task{name}")
# task("A")
# task("B")

# using threads
import time
import threading
def task(name):
    print(f"Started {name}")
    time.sleep(2)
    print(f"finished {name}")

t1=threading.Thread(target=task,args=("A",))
t2=threading.Thread(target=task,args=("B"))
t1.start()
t2.start()
t1.join()
t2.join()