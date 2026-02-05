#practicing class,object and inheritanec
lst=["server1","server2","server3"]
class app1():
    def __init__(self,cpu,mem):
        self.cpu=cpu
        self.mem=mem
    def patching(self,customscript,servername):
        if self.cpu >= 2 and self.mem >=4:
            print(f"{servername} is eligible for patching")
        else:
            customscript
            print(f"Changing the configuration using {customscript}")
    def build(self,servername):
        if servername in lst:
            print(f"{servername} is eligible for build")
        else:
            lst.append(servername)
class app2(app1):
    def decom(self,servername):
        if servername not in lst:
            print(f"{servername} is not in the lst you can proceed for decom")
        else:
            print("you are decommisioning the prodcution server")

prod=app2(3,4) # object creation
while True:
    print("Displaying the options for you")
    print("1.. Build")
    print("2.. Decommission")
    print("3.. Patching")
    print("4.. Exit the process")

    choice=int(input("Enter your choice of action:"))
    if choice == 1:
        prod.build(input("Enter the servername"))
    elif choice == 2:
        prod.decom(input("Enter the servername"))
    elif choice == 3:
        prod.patching("script",input("Enter the servername"))
    elif choice == 4:
        print("Exiting.....")
        break
    



        

