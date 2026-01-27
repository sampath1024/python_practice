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


def digitize(n):
    return list(map(int, str(n))).reverse
digitize(35231)
