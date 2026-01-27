#Take a number as input and check whether it is a single-digit, double-digit, or more than two-digit r
a=int(input("Enter a number:"))
if a>0 and a<=9:
    print("a is single digit")
elif a>=10 and a<=99:
    print("a is a double digit")
elif a>99:
    print(" a is more than two-digit number")
else:
    print("negative values")

