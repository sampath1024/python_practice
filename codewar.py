# def find_needle(haystack):
#     if "needle" in haystack:
#         p=haystack.index("needle")
#         print(f"found the needle at the position {p}")
# haystack=["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
# find_needle(haystack)

# def opposite(number):
#     if number >0:
#         number=-(number)
#         return number
#     elif number<0:
#         number=number*(-1)
#         return number
#     else:
#         print("Enter the positive values:")
# opposite(1)

# def bmi(weight, height):
#     bmi1=(weight)/(height ** 2)
#     if bmi1<= 18.5:
#      return "Underweight"
#     elif bmi1 <= 25.0:
#      return "Normal"
#     elif bmi1 <= 30.0:
#      return "Overweight"
#     elif bmi1>30:
#      return "Obese"
#     else:
#      return "positive values"
# bmi(50,1.80)

# def number_to_string(num):
#     return str(num)
# print(number_to_string(123))
# lst=['hello', 'world', 'this', 'is', 'great'] 
# result=' '.join(lst)
# print(result)
# def count_by(x,n):
#     result=[]
#     for i in range(1,n+1):
#         result.append(x*i)
#     return result


# def count_by(x,n):
#     return [x*i for i in range(1,n+1)]
# print(count_by(1,5))
# def digitize(n):
#     return 'n'.split()
# print(digitize("sampath"))


# def digitize(n):
#     return list(map(int, str(n))).reverse
# prindigitize(35231)

# def double_integer(i):
#     print (i*2 if i>=0 else None)
# double_integer(-10)

# def double_integer(i):
#     print (i*2)
# double_integer(-10)

# def lovefunc( flower1, flower2 ):
#     if flower1 % 2 !=0 & flower2 %2 ==0:
#          print(True)
#     else:
#         print(False)
# lovefunc(0,1)

# def invert(lst):
#     for i in lst:
#         lst.append(-i)
#         print(lst)
# lst=[1,2,3,4,5]
# invert(lst)

def count_sheep(n):
    if n==0:
        return ""
    elif n in range(n+1,start=1):
        print(f"{n} sheep...")
count_sheep(5)
