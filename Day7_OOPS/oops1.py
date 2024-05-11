#Example 1:
#create the class and metjod inside the class
class MyClass:
    def myfun(self):
        pass
    def display(self,name):
        print(name)


#create the object
mc1=MyClass()
mc2=MyClass()

mc1.myfun()
mc1.display("Jhonson")

#Example 2: Create Instance method and static method
class MyClass2:
    def m1(self):
        print("This is Instance method")

    @staticmethod
    def m2(self,num):
        print("This is static method :",self,num)

mc1=MyClass2()
mc1.m1()                             #calling the instance method using object

MyClass2.m2(10,20)        #calling the static method using class name only


#Example 3:
class MyClass3:
    a,b=10,20            #class variables

    def add(self):
        print(self.a+self.b)   #to asscec the class variables inside the method used 'self' keyword. self represent the class namee
    def mul(self):
        print(self.a*self.b)

mc3=MyClass3()
mc3.add()
mc3.mul()

#Example 4:
i,j=15,20                 #global variable

class MyClass4:
    a,b=30,40             #class variables
    def add(self,x,y):    #local variables
        print(x+y)           #x and y are local varaibles access
        print(self.a+self.b) # a and b are class varaible assecc using self keyword
        print(i+j)           #i and j are gloabal variable can used

mc4=MyClass4()
mc4.add(100,200)


#Example 5: all three varaibles name is same
a,b=15,20                 #global variable
class MyClass5:
    a,b=30,40             #class variables
    def add(self,a,b):    #local variables
        print(a+b)                                #access local no issue
        print(self.a+self.b)                      #access class varaibles by using self
        print(globals()['a']+globals()['b'])      #to access the global variables use globals function

mc5=MyClass5()
mc5.add(100,200)


#Exmples 6 : one class can have multiple objects
class MyClass6:
    def display(self,name):
        print("This is display...")
        print(name)

obj1=MyClass6()
obj1.display("Jhon")

obj2=MyClass6()
obj2.display("Ram")


#Example 7: Constructer
class MyClass7:
    def __init__(self):
        print("This is constructor..")
    def m1(self):
        print("Hello")
    def m2(self,x,y):
        return (x+y)

mc7=MyClass7()         #this statment automatically invoke the constructor
mc7.m1()               #object always needed to invoke the method
res=mc7.m2(10,20)
print(res)
