import os
filename = "sample.txt"
# if we are not assigning to any variable we can create by writing like file= open("sample.txt","w")
#write
file = open(filename,"w")
file.write("Hello Python\n")
file.write("Welcome to File Handling\n")
file.write("This is the third line.\n")
file.close()
#read
file = open(filename,"r")
print(file.read())
file.close()
#append
file = open(filename, "a")
file.write("This line is added using append mode.\n")
file.close()
#read operation stored in other variable
file = open(filename,"r")
content = file.read()
print(content)
file.close()
#readline
file = open(filename,"r")
print(file.readline())
print(file.readline(),end="") #to avoid new line
print(file.readline())
file.close()
#readlines
file = open(filename,"r")
print(file.readlines())
file.close()
#built-in -function if file exists or not
if os.path.exists(filename):
    os.remove(filename)
    print("Deleted successfully")
else :
    print(" Does not existed")   
#Display of characters or printing write operation
file = open(filename,"w")
content = file.write("python File Handling")
print(content)
# using with we need not to close the file
with open(filename, "r") as file:
    print(file.read())

