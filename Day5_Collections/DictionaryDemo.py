#Example1: Create dictionary
dic1={101:"x",102:"y",103:"z",104:"w"}
print(dic1)

#Example2: Asscess the items from the dictionary
dic2={
    "brand":"Hyundai",
    "Model":103,
    "Year":2021
      }
print(dic2["brand"])
print(dic2["Model"])
print(dic2["Year"])

#Using get() function
x=dic2.get("brand")
print(x)

#Example3: change the value of items in the dictionary
dic3={
    "brand":"Hyundai",
    "Model":103,
    "Year":2021
      }
print(dic3)             #{'brand': 'Hyundai', 'Model': 103, 'Year': 2021}
dic3["Year"]=2023
print(dic3)            #{'brand': 'Hyundai', 'Model': 103, 'Year': 2023}

#Example4: Reading items from the dictionary using looping statment
dic4={
    "brand":"Hyundai",
    "Model":103,
    "Year":2021
      }

#to extarct on keys from the dictionary
for i in dic4:
    print(i)

#to extarct on values from the dictionary
#Approach1
for i in dic4:
    print(dic4[i])

#Approach2
for i in dic4.values():
    print(i)

#to extarct Keys along with the values from the dictionary
for x,y in dic4.items():
    print(x,y)

#Example5: Check if the key is existing or not in dictionary
dic5={
    "brand":"Hyundai",
    "Model":103,
    "Year":2021
      }

#Appreoach 1
if "Model" in dic5:
    print("Exist !!!!")
else:
    print("Not Exist !!!!!!!")

#Approach 2
print("Model" in dic5)

#Example6: Findout total number of items in dictionary
dic6={
    "brand":"Hyundai",
    "Model":103,
    "Year":2021
      }
print(len(dic6))

#Example7: Adding the items in dictionary
dic7={
    "brand":"Hyundai",
    "Model":103,
    "Year":2021
      }
dic7["Colour"]="Red"
print(dic7)


#Example8: Remove the items in dictionary
dic8={
    "brand":"Hyundai",
    "Model":103,
    "Year":2021
      }
#Method1: using pop() function
dic8.pop("Model")
print(dic8)

#Method1: using del keyword
del dic8["Year"]
print(dic8)

#Example9: clear and delete the dictionary
dic9={
    "brand":"Hyundai",
    "Model":103,
    "Year":2021
      }
dic9.clear()
print(dic9)

#del dic9
#print(dic9)

#Example10: Copy the item fro  one dictionary to other
#Approach1 : without using copy() function
dic10={
    "brand":"Hyundai",
    "Model":103,
    "Year":2021
      }

dic11=dic10
print(dic11)

#Approach 2: Using copy()
dic12={
    "brand":"Hyundai",
    "Model":103,
    "Year":2021
      }
dic13=dic12.copy()
print(dic13)






