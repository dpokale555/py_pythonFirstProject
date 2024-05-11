#Example 1: Writing a data in text file
file=open("C:\DemoFIle\myfile.txt",'w')
file.write("This is my first statements..\n")
file.write("This is my second statements..\n")
file.write("This is my thid statements..\n")
file.write("This is my fourth statements..\n")
file.close()
print("Program completed")

#Example 2: Reading a data from text file
file=open("C:\DemoFIle\myfile.txt",'r')
#print(file.read())                #Reading all the data
print(file.readline())             #Reading the line first statment will print

file.close()

#Example 3: appending the data in text file/Adding new lines with existing new line
file=open("C:\DemoFIle\myfile.txt",'a')
file.write("This is my fifth line..\n")
file.write("This is my sixth line..\n")
file.close()
print("New Line added successfully")

