#Lists definition and properties
'''
1 Lists are mutable, ordered sequence data types
2 elements can be of different data types
3 can be used in [] and separated by ,
4 we can write list inside a list
'''
# list1=["sampath",29,164.5,[98,99,100]]
# # list2=set(list1)
# # print(list2)
# # print(type(list2))

# print(type(list1))
# print(list1)
# update=list1.append(30)
# print(list1)
# update1=list1.append({"data":100})
# print(list1)

#list to set conversion

# list2=set(list1)
# print(list2)
# print(type(list2))


# tuples practice
'''
1 tuples are immutable, ordered sequence of elements
2 similar to lists but can't be modified
3 defined in ()
'''
# tuple1=(5154, 3990, 8503,[45,56,67],("sampath","shekar","soujanya"),{99,99,100,101},{"name":"sampath"})
# print(tuple1)
# print(type(tuple1))

# sets practice
'''
1 Set is a unordered collection of unique elements
2 set itself is a mutable datatype, but it contains only immutable data types

'''
# set1={"name","value",99,99,100,477474}
# print(set1)

# tuple_conv=tuple(set1)
# print(type(tuple_conv))
# list_conv=list(tuple_conv)
# print(type(list_conv))

#dictionary practice
'''
1 ordered collectin of key value pairs
2 keys must be unique within a dictoinary
3 values can be duplicate
4 keys can be used only immutabel data types
5 converting a dict to tuple, only prints keys

'''

movie_budget={
"baahubali": 200,
"pushpa": {"pushpa1":{"director":50,"producer":50},"pushpa2":200},
"salar": 300
}
print(movie_budget)
tupl_conv=tuple(movie_budget)
print(tupl_conv)
print(type(tupl_conv))





