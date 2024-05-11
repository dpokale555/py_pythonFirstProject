#Example 1: Creating Tuple
mytuple=()             #empty tupled
mytuple1=("apple","banana","kiwi")
print(mytuple1)

#Example 2: Asscess items from Tuple
mytuple2=("apple","banana","kiwi","Cherry")
print(mytuple2[1])
print(mytuple2[-1])

#Example 3: Range of index
mytuple3=("apple","banana","kiwi","Cherry","Melon","Mango")
print(mytuple3[2:5])
print(mytuple3[-4:-1])

#Example 4: change the tuples items
#Tuple is immutable variables hence can not change
#We can not modified the existing value
#We can not append the new value
#We can not insert the new value
#We can not remove the value
#We can not copy the values


#but thiere is one way by converting tuple to list
mytuple4=("apple","banana","kiwi","Cherry","Melon","Mango")
mylist=list(mytuple4)
mylist.append("orange")
mytuple5=tuple(mylist)
print(mytuple5)

#Example 5: Reading tuples using for loop
mytuple5=("apple","banana","kiwi","Cherry","Melon","Mango")

for i in mytuple5:
    print(i)

#Example 6: Check if item is present or not
mytuple6=("apple","banana","kiwi","Cherry","Melon","Mango")

if "banana" in mytuple6:
    print("Item is present")
else:
    print("item is not present")

#Example 7: Check the length of the tuple
mytuple7=("apple","banana","kiwi","Cherry","Melon","Mango")
print(len(mytuple7))

#Example 8: Add value is not possible in tuples hence it won't work got the error
# mytuple8=("apple","banana","kiwi","Cherry","Melon","Mango")
# mytuple8[0]="orange"
# print(mytuple8)

#Example 9: Copy the one tuple value into other tuple
mytuple9=("apple","banana","kiwi","Cherry","Melon","Mango")
mytuple10=mytuple9

print(mytuple10)

#Example 10: Removing the items from the tuples can not possible
mytuple11=("apple","banana","kiwi","Cherry","Melon","Mango")
#mytuple11.remove("apple")    #it is Invalid can not work in tuple

#but we can delete the tuple
#del mytuple11
print(mytuple11)    #NameError: name 'mytuple11' is not defined.

#Example 11: Joining/Combining of tuples
mytuple12=("apple","banana","kiwi","Cherry","Melon","Mango")
mytuple13=(10,20,30,40)
mytuple14=mytuple12+mytuple13
print(mytuple14)

#Example 12: compaired the tuples
mytuple15=("apple","banana","kiwi","Cherry","Melon","Mango")
mytuple16=(10,20,30,40)

if mytuple15==mytuple16:
    print("Tuples are equals")
else:
    print("Tuples are not equals")


