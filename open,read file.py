# read and open file

file = open (r"C:\Users\Dell\Desktop\Python\F_O\data.txt","r")
content = file.read()
print(content)
file.close()

# readline()

file = open (r"C:\Users\Dell\Desktop\Python\F_O\data.txt","r")
print(file.readline())
file.close()

# readlines()

file = open (r"C:\Users\Dell\Desktop\Python\F_O\data.txt","r")
print(file.readlines())
file.close()