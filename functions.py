#Function practice
#syntax
#def functionname():
       #block of code
#functionname() # function calling

def condition():
    a=10
    b=9
    if a == b:
        return True
    else:
        return False
print(condition())

#if we use return in a function, it will exit the funtion and returns the value to the caller
#if we want to view the value, we can print the calling function
def details(**name):
    return f"Name is {name}"
print(details(name="sampath", age=30 , role="cloud"))


