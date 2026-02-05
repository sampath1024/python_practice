#Super market billing
Product_list={
     "Rice" : 100,
     "Wheat" : 150,
     "Sugar" :  90,
     "Soap" : 10
}
cart=[]
price=[]
#Display a list of available products with their prices
print("Available Items in our supermarket:")
print("=================")
lst=Product_list.items()
print("Item","\t" "price")
print("=================")
for i,j in lst:
    print(i,"\t",j)
# product selection
while True:
    product_name=input("Enter the product to buy:")
    if product_name == "Rice":
        cart.append(product_name)
        quantity=input("Enter the quantity:")
        if quantity.isdigit():
            q=int(quantity)
            print(f"Entered quantity is {q} ")
            rice_price=Product_list[product_name] * q
            price.append(rice_price)
            print(f"Price of {product_name} is: {Product_list[product_name] * q}")
        else:
              print("Please enter the valid quantity")
    elif product_name == "Wheat":
         cart.append(product_name)
         quantity=input("Enter the quantity:")
         if quantity.isdigit():
            q=int(quantity)
            print(f"Entered quantity is {q} ")
            wheat_price=Product_list[product_name] * q
            price.append(wheat_price)
            print(f"Price of {product_name} is: {Product_list[product_name] * q}")
            
    elif product_name == "Sugar":
         cart.append(product_name)
         quantity=input("Enter the quantity:")
         if quantity.isdigit():
            q=int(quantity)
            print(f"Entered quantity is {quantity} ")
            sugar_price= Product_list[product_name] * q
            price.append(sugar_price)
            print(f"Price of {product_name} is: {Product_list[product_name] * q}")
    elif product_name == "Soap":
         cart.append(product_name)
         quantity=input("Enter the quantity:")
         if quantity.isdigit():
            q=int(quantity)
            print(f"Entered quantity is {quantity} ")
            soap_price=Product_list[product_name] * q
            price.append(soap_price)
            print(f"Price of {product_name} is: {Product_list["Soap"] * q}")
    
    else:
            print("Given product is not available in Store ")
            break
    
    print(f"Items added in the cart with price {cart}:{price} ")
    #Billing and Calculations:
    print(f"Purchased Items list with thier prices:{cart}:{price}")



    



