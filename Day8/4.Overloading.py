#Example 10: Overloading (POlymorpyisum)
class Human:
    def sayhello(self,name=None):
        if name is not None:
            print("Hello "+name)
        else:
            print("Hello, User")

h=Human()
h.sayhello()
h.sayhello("Ram")

#Example 11: Overloading (POlymorpyisum)
class Calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)

cal=Calculation()
cal.add()
cal.add(10,20)
cal.add(10,20,30)

