#Example 1: Create set
myset1={"apple","Banana","Kiwi"}
print(myset1)

#Example2: Accessing items value from the set
myset2={"apple","Banana","Kiwi"}
for i in myset2:
    print(myset2)

#Example3: Check if value is exist is or not
myset3={"apple","Banana","Kiwi"}
print("Banana" in myset3)
print("Banana2" in myset3)

#Example4: Add the items in set add() and update()
#Method1: using add() functions
myset4={"apple","Banana","Kiwi"}
myset4.add("Grape")
print(myset4)

#Method2: using update() functions
myset5={"apple","Banana","Kiwi"}
myset5.update(["mango","Melon"])
print(myset5)

#Example5: Findout the number of values
myset6={"apple","Banana","Kiwi"}
print(len(myset6))

#Example6: Remove the items from set
#Using remove() functions
myset7={"apple","Banana","Kiwi"}
myset7.remove("Banana")
print(myset7)

#diffrence beetwin remove() and dicard() function is if try to removeing non existance item from the set while using remove() function throw the error.

#Using discard() functions
myset8={"apple","Banana","Kiwi"}
myset8.discard("Banana")
print(myset8)

#Example7: Clear the items from set
#1) Using clear() function
myset9={"apple","Banana","Kiwi"}
myset9.clear()
print(myset9)

#2) using del keyword
# del myset9
# print(myset9)

#Example8: Joining the 2 sets
#Method1: using union() function
myset10={"A","B","C"}
myset11={1,2,3}
myset12=myset10.union(myset11)
###OR###
myset122=myset10 | myset11
print(myset12)
print(myset122)

#Method1: using update() function
myset13={"A","B","C"}
myset14={1,2,3}
myset13.update(myset14)
print(myset13)

#Example : common and uncommon items
myset15={4,2,5,6,7}
myset16={1,2,3,6,9}
print(myset15 & myset16)
print(myset15 - myset16)
print(myset16 - myset15)








