#practicing file handling
#r -- read (opens an existnig file for read operation)
#w -- write(open for write operation, but it will ovveride the information and also file gets created if not present)
#a -- append(open and appends, it won't ovveride)

# file=open("sample.txt","r+")
# file.write("Hello")
# print(file.tell())
# file.seek(0)
# print(file.read())
# file.close()


# file=open("sample.txt","w+")
# file.write("Hello")
# print(file.tell())
# file.seek(0)
# print(file.read())
# file.close()

# file=open("sample.txt","a+")
# file.write("Hello1")
# print(file.tell())
# file.seek(0)
# print(file.read())
# file.close()

# file=open("sample.txt","w+")
# file.write("hello1")
# file.seek(0)
# print(file.read())
# file.close()

#chaging the file name
import os
#os.rename("sample.txt", "new.txt")
os.remove("new.txt")







