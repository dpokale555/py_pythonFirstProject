#Example 1 : How to create list

mylist1 =[10,20,30,40,50]
mylist2 =["Apple","Banana","Cherry"]
mylist3 =["Papaya",20,30.5]
mylist4=list()               #Create empty list

print(mylist1)
print(mylist2)
print(mylist3)
print(mylist4)

#Example 2 : Assecc the items from the list
mylist5 =["Apple","Banana","Cherry","Papaya"]
print(mylist5[0])                    #Apple
print(mylist5[2])                    #Cherry
print(mylist5[-1])                   #Papaya
print(mylist5[-2])                   #Cherry

#Example 3 : How to create list
mylist6 =["Apple","Banana","Cherry","Papaya","Mango","Melon","Kiwi"]
print(mylist6[2:5])                #['Cherry', 'Papaya', 'Mango']

print(mylist6[-4:-1])              #['Papaya', 'Mango', 'Melon']

#Example 4: How to change item value from the list
mylist7 =["Apple","Banana","Cherry","Papaya","Mango","Melon","Kiwi"]
print(mylist7)
mylist7[0]="orange"          #this will change the values based on index
print(mylist7)

#Example 5: How to read the list items using loop statment
mylist8 =["Apple","Banana","Cherry","Papaya","Mango","Melon","Kiwi"]

for i in mylist8:
    print(i)

#Example 6: How to read the list items using loop statment
mylist9 =["Apple","Banana","Cherry","Papaya","Mango","Melon","Kiwi"]

if "Apple" in mylist9:
    print("The items is present")
else:
    print("The item is not present")

#Example 7: List length (counting the numbers of items present in lists)
mylist10 =["Apple","Banana","Cherry","Papaya","Mango","Melon","Kiwi"]
print(len(mylist10))

#Example 8: To add the new items in a list: append() and insert()
mylist11 = ["Apple","Banana","Cherry","Papaya","Mango","Melon","Kiwi"]
mylist11.append("orange")
print(mylist11)

mylist11.insert(3,"Grape")
print(mylist11)

#Example 9: To remove the items from a list: pop() and keyword 'del'
#Functions : pop()
mylist12 = ["Apple","Banana","Cherry","Papaya","Mango","Melon","Kiwi"]
mylist12.pop(2)
print(mylist12)

#keyword : del
mylist13 = ["Apple","Banana","Cherry","Papaya","Mango","Melon","Kiwi"]
del mylist13[4]
print(mylist13)

#Functions : clear()
mylist14 = ["Apple","Banana","Cherry","Papaya","Mango","Melon","Kiwi"]
mylist14.clear()
print(mylist14)

#Example 10: To copy the items from a list
#approach 1: Using 'list()' functions
mylist15 = ["Apple","Banana","Cherry","Papaya","Mango","Melon","Kiwi"]
mylist16=list(mylist15)
print(mylist15)
print(mylist16)

#approach 2: Using 'copy()' functions
mylist17 = ["Apple","Banana","Cherry","Papaya","Mango","Melon","Kiwi"]
mylist18=mylist17.copy()
print(mylist17)
print(mylist18)

#Example 11: To combine/joins the two lists
#approach 1: Using '+' operators
mylist19 = ["A","B","C","P"]
mylist20 =[10,20,30,40,50]
mylist21=mylist19+mylist20
print(mylist21)

#approach 2: Using for loops
mylist22 = ["A","B","C","P"]
mylist23 =[10,20,30,40,50]
for i in mylist23:
    mylist22.append(i)
print(mylist22)

#approach 2: Using extend() functions
mylist24 = ["A","B","C","P"]
mylist25 =[10,20,30,40,50]
mylist24.extend(mylist25)
print(mylist24)

#Example 12: compaired the Lists
mylist25=[10,20,30,40]
mylist26=[10,20,30,40]

if mylist25==mylist26:
    print("Lists are equals")
else:
    print("Lists are not equals")

#Example 13: Create the list using some rules
#Rule 1: Create the list of Square
List1=[x**2 for x in range(10)]
print(List1)

#Rule 2: create the list of only even square
List2=[x**2 for x in range(10) if x**2 % 2==0]
print(List2)

#Rule 3: create the list of only odd square
List2=[x**2 for x in range(10) if x**2 % 2!=0]
print(List2)

#Example 14: Join function for list
print("".join(["Apple","Banana","Kiwi"]))
print(",".join(["Apple","Banana","Kiwi"]))

List1=["Mango","Melon","Grape"]
print(" | ".join(List1))