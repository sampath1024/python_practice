#syntax
#class cn():
    #class body 
    #attr
    #methods


# class person_details():#class definition
#     user = "kiran" #attributes
#     user_id = 1234 #attributs
#     def details(self,): #methods
#         print(f"working at MNC company {self.user}")
#     def details_2(self,): #methods
#         print(f"he runs ABC company id was {self.user_id}")
#         self.details()
#syntax
# objname = classname()
# kiran_kumar = person_details()
# kiran_kumar.details()
# kiran_kumar.details_2()
# print(kiran_kumar.user)
# print(kiran_kumar.user_id)




# user = "vasu"
# def sample(a):
#     print("sample statement")
#     print(user)
# sample(100)



# class feature_phone():
#     bn = "nokia"
#     color = "white"
#     model = "2015"
#     def calling(self,brandname):
#         print(f"you are calling from.......{brandname}")
#     def message(self,mn):
#         print(f"message sent successfully {mn}...")
# #syntax
# # objname = classname()
# nokia = feature_phone()
# nokia.calling("nokia")
# nokia.message(1234567890)


# nokia_2016 = feature_phone()
# nokia_2016.calling("nokia_2016")
# nokia_2016.message(1231564950)


# microsoft = feature_phone()
# microsoft.calling("microsoft")




# class feature_phone():
#     def __init__(self,bn,color,model):
#         self.bn = bn
#         self.color = color
#         self.model = model
#     def calling(self,):
#         print(f"you are calling from.......{self.bn}")
#     def message(self,mn):
#         print(f"message sent successfully ...{mn}")

# nokia = feature_phone("nokia","white",2012)
# nokia.calling()
# nokia.message(1234)
# microsoft = feature_phone("lumia","black",2013)
# microsoft.calling()
# microsoft.message(16498456)








# class feature_phone():
#     def __init__(self,bn,color,model):
#         self.bn = bn
#         self.color = color
#         self.model = model
#     def calling(self,):
#         print(f"you are calling from.......{self.bn}")
#     def message(self,mn):
#         print(f"message sent successfully ...{mn}")
# class smartphone(feature_phone):
#     def browsing(self,browser):
#         print(f"you are browsing internet {browser}. ..")
# obj = smartphone("nokia","white",2020)
# obj.calling()
# obj.message(131564)
# obj.browsing("chrome")





# class a():
#     def parent(self):
#         print("this is parent class")
# class b(a):
#     def child1(self):
#         print("this is child 1 class")
# class c(a):
#     def child2(self):
#         print("this is child 2 class")

# obj = b()
# obj.parent()
# obj.child1()



# obj = c()
# obj.parent()
# obj.child2()




# class gfather():
#     def output(self):
#         print(f"earned 100cr properties")
# class father(gfather):
#     def output1(self):
#         print(f"this is father class")
# class child(father):
#     def output2(self):
#         print(f"this is child class")
#     def sample(self):
#         print(f"startef ABC company")

# obj = child()
# obj.output()
# obj.output1()
# obj.output2()
# obj.sample()











# class parent1():
#     def father(self):
#         print("this is father class")
# class parent2():
#     def mother(self):
#         print("this is mother class")
# class child(parent1,parent2,):
#     def child(self):
#         print("this is child class")

# obj = child()
# obj.mother()
# obj.father()
# obj.child()




# ATM
# class ATM():
#     def __init__(self,bankname,branch,model,balance = 1000):
#         self._balance = balance
#         pass
#     def account(self,user,password):
#         self.user = user
#         self.__password = password
#     def deposist(self,):
#         pass
#     def withdraw(self,):
#         pass
#     def balance(self,):
#         pass
# class ATM2(ATM):
#     def ministatment(self):
#         pass
# SBIN = ATM2()




###########   jan 20 2026 ###############








# Polymorphism

#polymorphism --> implementing same thing in different forms

#1..overloading --> 1.operator overloading 2.method overloading
#2. method overriding


# 1.operator overloading
# (+)
# a = 10
# b = 20
# print(a+b)

# a = "kiran"
# b = "raju"
# print(a+b)



#method overloading --> method name should be same
#arguments must be different --> in the terms of length or type of arguments

# class calculator():
#     def add(self,a,b):
#         print(a,b)
#     def add(self,a,b,c):
#         print(a,b,c)
    
# obj = calculator()
# obj.add(10,10)
# obj.add(10,10,10)


# class calculator():
#     def add(self,a=None,b=None,c=None):
#         print(a,b,c)

# obj = calculator()
# obj.add(10,10,10)
# obj.add(10,10)
# obj.add(10)
# obj.add()
# obj.add("kiran","sampath","raju")
# obj.add("kiran","sampath",)
# obj.add("kiran",)
# obj.add("kiran",25,5.7)






# method overriding --> method name should be same arguments should be also same length

# class gfather():
#     def details(self,):
#         print(f"this is gfather class")
    
# class father(gfather):
#     def details(self,):
#         print(f"this is father class")
#         super().details()
# obj = father()
# obj.details()




# Public  
# protect _
# private __


# class gfather():
#     def __init__(self,a):
#         self._a = a
#         print(f"this is base class {a}")
# class father(gfather):
#     def display(self):
#         print(f"this is father derived class {self._a}")

# obj = father("100cr")
# obj.display()




# class gfather():
#     def __init__(self,a):
#         self.__a = a
#         print(f"this is base class {a}")
# class father(gfather):
#     def display(self):
#         print(f"this is father derived class {self.__a}")

# obj = father("100cr")
# obj.display()









#data abstraction --> hiding the implementation and showing only essential part


# 1.abstract class --> class which contain abstract methods is called abstract class
# 2.abstract method --> the method which is having only declaration but not the definition is called abstract method (hiding the implementation)
# class which does not have abstract method is called concrete class
# concrete class  --> class without abstract methods
# object cannot create for abstract class
# object can create only concrete classes
# To create abstract classes in Python, you can use the abc (Abstract Base Classes) module


# from abc import ABC,abstractmethod
# class abstract_demo(ABC):
#     @abstractmethod
#     def display(self,):
#         pass
#     @abstractmethod
#     def display2(self,):
#         pass

# class demo(abstract_demo):
#     def display(self,):
#         print(f"implementation done")
#     def display2(self):
#         print(f"implementation 2 done")
# obj = demo()
# obj.display()
# obj.display2()


# from abc import ABC,abstractmethod
# class payment(ABC):
#     @abstractmethod
#     def payment(self):
#         pass

# class gpay(payment):
#     def payment(self):
#         print(f"payment done via gpay")

# class phonepe(payment):
#     def payment(self):
#         print(f"payment done via phonepe")
    
# class cred(payment):
#     def payment(self):
#         print(f"payment done via cred")
#     def payment2(self):
#         print(f"1 cashback received")

# obj = phonepe()
# obj.payment()

# obj2 = gpay()
# obj2.payment()