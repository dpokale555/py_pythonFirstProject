#Example1
print("This is starting statment of program1")
print("This is starting statment of program1")
print("This is starting statment of program1")
try:
    print(x)
except:
    print("Exception occured")
print("This is starting End of program2")
print("This is starting End of program2")
print("This is starting End of program2")

#Example 2:
print("This is starting point of program..")
print("Program in progress")
try:
    print(10/0)
except ZeroDivisionError:
    print("ZeroDivisionError Occured and handled")
print("Program completed...")

#Example 3: Multiple except block -- try, except, else, finally

# try:
    num1,num2=10,
    result=num1/num2
    print("result is :", result)
# except ZeroDivisionError:
#     print("ZeroDivisionError occured and handled")
# except SyntaxError:
#     print("SyntaxError occured and handled")
# except IndentationError:
#     print("IndentationError occured and handled")
# except :
#     print("Exception occured and handled")
# else:
#     print("No Exception occured")
# finally:
#     print("Always execute this block")

#Example 4: Raising our own exception: User define exception
def entiger(num):
    if num<0:
        raise ValueError("Only positive Integers are allowed")
    if num%2==0:
        print("Even Number")
    else:
        print("Odd Number")

print("Checking if the passing number is odd/even")
num=-3
try:
    entiger(num)
except ValueError:
    print("ValueError exception occured and handeled")

print("Program completed")




