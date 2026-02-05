#logic building using loops
#print all numbers from 1 to 10
# count=1
# while count<=10:
#     print(count)
#     count+=1

# # 10 to 1
# count = 10
# while count>=1:
#     print(count)
#     count-=1

# #print all even numbers from 1 to 100
# class numbers():
#     def even(self,):
#      for i in range(1,101):
#         if i%2==0:
#             print(i)
#     def odd(self,):
#        for i in range(1,101):
#           if i%2!=0:
#              print(i)

# detect=numbers()
# detect.odd()
#even or odd using while loop
# i=1
# while i<=101:
#     if i%2==0:
#         print(f"Number {i} is even")
#     else:
#         print(f"Number {i} is odd")
#     i+=1
#multiplication table of a given number from nX1 to nX10
# i=int(input("Enter a number:"))
# j=1
# while True:
#     while j<=10:
#         print(f"{i}X{j}={i*j}")
#         j+=1
#     break

#calculate and print the first n natural numbers
# total=0
# n=int(input("Enter a number:"))
# i=1
# while i<=n:
#     total+=i
#     i+=1
# print("Sum:",total)
#calculate the sum of all even numbers from 1 to n
# total=0
# n=int(input("Enter a number:"))
# i=1
# while i<=n:
#     i+=1
#     if i%2==0:
#         total+=i
#     else:
#         print("exiting...")
#     print(total)





class serverbuild():
    def __init__(self,domain,company):
        self.domain=domain
        self.company=company
    def patching(self,):
        print(f"This block for server patching {self.company}")
    def provisioning(self,):
        print(f"This block is for provisioning")

obj=serverbuild("optum.com","optum")
obj.patching()










