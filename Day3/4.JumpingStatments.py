#Example 1:
for i in range(0,10):
    if i==5:
        break
    print(i)
print("Program stop1")

#Example 2:
for i in range(0,10):
    if i==5:
        continue
    print(i)
print("Program stop2")

#Example 3:
for i in range(0,10):
    if i==3 or i==5 or i==8:
        continue
    print(i)
print("Program stop3")

#Example 4:
for i in range(3,7,2):
    if i==4:
        continue
    print(i)
print("Program stop4")