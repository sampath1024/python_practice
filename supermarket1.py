#Super market billing
Product_list={
     "Rice" : 100,
     "Wheat" : 150,
     "Sugar" :  90,
     "Soap" : 10
}
cart=[]
while True:
    #Display a list of available products with their prices
    print("Available Items in our supermarket:")
    print("=================")
    lst=Product_list.items()
    print("Item","\t" "price")
    print("=================")
    for i,j in lst:
        print(i,"\t",j)
    # product selection
    product_name=input("Enter the product to buy:")
    if product_name == "Rice":
        print(f"Price of {product_name} is:")
        print(Product_list["Rice"])
        cart.append(product_name)
    elif product_name == "Wheat":
        print(f"Price of {product_name} is:")
        print(Product_list["Rice"])
        cart.append(product_name)
    elif product_name == "Sugar":
        print(f"Price of {product_name} is:")
        print(Product_list["Rice"])
        cart.append(product_name)
    elif product_name == "Soap":
        print(f"Price of {product_name} is:")
        print(Product_list["Rice"])
        cart.append(product_name)
    else:
        print("Given product is not available in Store ")
        




#Allow users to add multiple items to their cart



