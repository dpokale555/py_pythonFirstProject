#Example1:
def fun1(i,j):
    print(i,j)

fun1(10,20)   #positional arugements
fun1(j=30, i=50)   #Keyword arguments

#Exanple2:
def fun2(i=10,j=20):
    print(i,j)

fun2()
fun2(100,200)             #default value will be replaced by input value

#Exanple3:
def fun2(i,j=20):
    print(i,j)

fun2(200)

#Exanple4:     Keyword arguements
def mesg(name,greetmsg):
    print(greetmsg+" "+name)

mesg(name='Jhon',greetmsg="Hello")
mesg(greetmsg="Hello",name='Jhon')

#Example5: comboination of positional and keyword argeuments
def my_fun(a,b,c):
    print(a,b,c)

my_fun(10,20,30)    #Positional Arrgeuments
my_fun(b=20,c=30,a=10)        #Keyword Arrgeuments
my_fun(10,20,c=30)     #Combination of both
my_fun(10,b=20,c=30)      #combinations of both
#my_fun(10,b=20,30)          #Invalid : Posotional arrgemunets should come before keyword arguements

#Example 6: Functions can return multiple values

def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a

print(largest(100,200))

