#Example 1: Single Inheritance
class A:
    def m1A(self):
        print("This is m1A from class A")

class B(A):
    def m1B(self):
        print("This is m1B from class B")

b_Obj=B()
b_Obj.m1A()
b_Obj.m1B()

#Example 2: Single Inheritance
class AA:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class BB(AA):
    a,b=100,200
    def m2(self):
        print(self.a-self.b)

bb_obj=BB()
bb_obj.m1()
bb_obj.m2()

#Example 3: Multilevel Inheritance
class X:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class Y(X):
    a,b=200,300
    def m2(self):
        print(self.a-self.b)

class Z(Y):
    i,j=2,4
    def m3(self):
        print(self.i*self.j)

z_Obj=Z()
z_Obj.m1()
z_Obj.m2()
z_Obj.m3()


#Example 4: Hierarchy Inheritance
class A1:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B1(A1):
    a,b=200,300
    def m2(self):
        print(self.a-self.b)

class C1(A1):
    i,j=2,4
    def m3(self):
        print(self.i*self.j)

b1_Obj=B1()
b1_Obj.m1()
b1_Obj.m2()

c1_Obj=C1()
c1_Obj.m1()
c1_Obj.m3()

#Example 5: Multiple Inheritance
class J:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class K:
    a,b=200,300
    def m2(self):
        print(self.a-self.b)

class L(J,K):
    i,j=2,4
    def m3(self):
        print(self.i*self.j)

l_Obj=L()
l_Obj.m1()
l_Obj.m2()
l_Obj.m3()