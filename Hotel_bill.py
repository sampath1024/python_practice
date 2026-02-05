Hotel_name="HOTEL MAITRI RESIDENCY\nBESIDE CIRCUS GROUND\nKARIMNAGAR - 505501\nCRYSTAL RESTAURANE"
#print(Hotel_name)
import datetime
item_list='''
1:Chicken Biryani 
2:Mutton Biryani 
3:Veg Biryani 

'''
print(item_list)
#CGST=SGST=0.025
#print(CGST)
item_price={"Chicken_biryani":1000,"Mutton_Biryani":250,"Veg_biryani":150}
choice=input("press 1 for list and press 2 for exit")
while True:
    if choice == 2:
        print("Thank you for visiting our hotel")
        break
    elif choice ==1:
        print(item_list)

        while True:
            option=input("Press 1 to buy and 2 to exit")
            if option == 2:
                print("Thank you for visiting our hotel")
                break
            elif option == 1:
                order=input("choose your order").lower()
                while True:
                    quant=input("Enter the qunatity:")
                    if quant.isdigit():
                        q=int(quant)
                        break
                    else:
                        print("Please enter the valid quntity")
                        



        price=item_price["Chicken_biryani"]
        print(f"You have choosen Chicken Biryani and its price is {price}")
    
    






