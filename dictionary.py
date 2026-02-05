#dict_practice
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(len(my_dict))

my_dict.update({'d':4})
print(my_dict)
my_dict = {'name': 'python', 'age': 30, 'city': 'Tadepalligudem'}
print(my_dict.keys())
#Task 1: Dictionary Update
'''
Write Python code to add a new key-value pair to the following dictionary:
my_dict = {'name': 'python', 'age': 25}
# Your code here
# Output should be: {'name': 'python', 'age': 25, 'city': 'we
st godavari'}

'''
my_dict = {'name': 'python', 'age': 25}
my_dict.update({"city":"west godavari"})
print(my_dict)
print(f"new dictionary value is:{my_dict}")
#Task 2: Dictionary Access
'''
Write Python code to access and print the value associated with the key 'price' in
the following dictionary:
Dictionary Quiz: 3
product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1
200}
# Your code here
# Output should be: 1200
'''
product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200}
print(product_info['price'])
#Task 3: Dictionary Removal
'''
Write Python code to remove the key-value pair with the key 'city' from the
following dictionary:
my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
# Your code here
# Output should be: {'name': 'John', 'age': 30}
'''
my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
my_dict.pop('city')
my_dict.update({'name':'John'})
print(my_dict)
#Task 4: Dictionary Keys
'''
Write Python code to print all the keys present in the following dictionary:
my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundr
y'}
# Your code here
# Output should be: ['name', 'age', 'city']

'''
my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
print(my_dict.keys())
#Task 5: Dictionary Values
'''
Write Python code to print all the values present in the following dictionary:
Dictionary Quiz: 4
my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
# Your code here
# Output should be: ['python', 25, 'tanuku']

'''
my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
print(my_dict.values())
#Exercise 1: Dictionary Update
'''
Write a Python script that updates a dictionary with a new key-value pair.
'''
car_data={
    "Toyota":2015,
    "Mariti":2016,
    "Kia":2018
}
car_data.update({"Tata":2019})
print(car_data)
#Exercise 2: Dictionary Access
'''
Write a Python script that accesses and prints the value associated with a specific
key in a dictionary.
'''
car_data={
    "Toyota":2015,
    "Mariti":2016,
    "Kia":2018
}
print(f"Toyota car model is: {car_data['Toyota']}")

#Exercise 3: Dictionary Removal
'''
Write a Python script that removes a key-value pair from a dictionary.
'''
car_data={
    "Toyota":2015,
    "Mariti":2016,
    "Kia":2018
}
car_data.pop("Toyota")
print(car_data)
#Exercise 4: Dictionary Keys 
#Exercise 5: Dictionary Values
'''
Write a Python script that prints all the keys present in a dictionary.
Write a Python script that prints all the values present in a dictionary.
'''
car_data={
    "Toyota":2015,
    "Mariti":2016,
    "Kia":2018
}
print(car_data.keys())
print(car_data.values())


