#Example 6: Overwriting of method using same method name
class A:
    def m1(self):
        print("This is m1 method from class A")

class B(A):
    def m1(self):
        print("This is m1 method from class B")
        super().m1()                              #this will invoke the parrent class method

b_Obj=B()
b_Obj.m1()      #By default invoiking the child class method only here

#Example 7:
class X:
    a,b=10,20
class Y(X):
    i,j=100,200
    def m(self,x,y):
        print(x+y)                    #Local Variables
        print(self.i+self.j)          #class variables from same class(Child)
        print(self.a+self.b)          #class variables from other class(Parent)

y_Obj=Y()
y_Obj.m(1000,2000)

#Example 8: Overriding the variables
#Senario 1: default print the latest value of variable from child class
class Parent1:
    name="Ram"
class Child1(Parent1):
    name="Karan"

c_obj1=Child1()
print(c_obj1.name)   #here, by default print the latest value of variable which means from child class

#Senario 2: Print the value of variable from the parrent class
class Parent2:
    name="Ram"
class Child2(Parent2):
    name="Karan"
    def test(self):
        print(super().name)

c_obj2=Child2()
c_obj2.test()   #here, print the variable value from the parrent class



#Example 9: Overriding the Methods
class Bank:
    def ROI(self):
        return 0

class XBank(Bank):
    def ROI(self):
        return 10

class YBank(Bank):
    def ROI(self):
        return 20

x_Obj=XBank()
print(x_Obj.ROI())

y_Obj=YBank()
print(y_Obj.ROI())






