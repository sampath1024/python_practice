lists = '''
Rice       Rs 10/kg
Sugar      Rs 8/kg
Oil        Rs 30/liter
Salt       Rs 25/kg
Paneer     Rs 40/kg
Maggie     Rs 12/pack
Boost      Rs 200/bottle
'''
# Declaration
price = 0
pricelist = []
totalprice = 0
Finalprice = 0
ilist = []
qlist = []
plist = []
# Rate for each item
items = {'rice': 10, 'sugar': 8, 'oil': 30, 'salt': 25, 'paneer': 40, 'maggie': 12, 'boost': 200}
def item_list():
    print("Below are the Items in our market")
    print("===================================")
    print(lists)
def item_choosing():
    choice=int(input("Press 1 for list or 2 to exit: "))
    if choice == 2:
        print("Thanks for shopping")
    elif choice == 1:
        item_list()
item_choosing()




        
