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

#Example 8: Constructer
class MyClass8:
    name="Ram"
    def __init__(self,name):   #constructor is expecting parameter/arguments
        print(name)            #for local variables
        print(self.name)       #for class variables use self

mc8=MyClass8("David")          #Passing parameter to the constructor

#Example 9:
#Req: Create one Emp class. Will have one constructore inside the class with eid, ename, sal and
# create one display() method which print eid, ename and sal

class Emp:

    def __init__(self, eid, ename, sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal
    def display(self):
        print(self.eid,self.ename,self.sal)

e1=Emp(101,"Jhon",20000)
e1.display()

e2=Emp(102,"David",30000)
e2.display()

#Example 10:
#Req: Create one Emp class. Will have one constructore inside the class with eid, ename, sal and
# create one more constructor to display which print eid, ename and sal

class Emp:

    def __init__(self, eid, ename, sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal
    def __str__(self):             #this constructor onlyu read the string type of value
        return(self.ename)


e1=Emp(101,"Jhon",20000)
print(e1)


