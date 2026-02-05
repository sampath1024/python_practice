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




#ATM
class ATM():
    def __init__(self,bankname,branch,balance = 1000):
        self.bankname=bankname
        self.branch=branch
        self.balance=balance
    def deposist(self,):
        pass
    def withdraw(self,):
        pass
    def balance(self,):
        pass
class ATM2(ATM):
    def ministatment(self):
        pass
SBIN = ATM2()