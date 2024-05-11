#Example1:
global_var1=100

def fun():
    local_ver1=20
    print(local_ver1)
    print(global_var1)

fun()
global_var2=30

#print(local_var1)    #Invalid : cannot used outside the function
print(global_var2)    #Valid : can used global variable outside the function

#Example2:
xy=100                    #Global Variable with 'xy' name
def cal():
    xy=200              #Local Variable with same name 'xy'
    print(xy)

cal()                   #In such case it will always used local variable from the function



#Example3:
xy=300
def cal():
    global xy
    xy=400
    print(xy)

cal()
print(xy)

#Example 4:
x=100
def cal():
    global x
    xy=200

#cal()
print(x)

#Example 5:
def cal():
    global x
    x=500
    print(x)

cal()
print(x)

