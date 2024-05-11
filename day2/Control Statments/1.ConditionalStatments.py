#if  if.....Else  elif

#Example 1 for if: Print if person is eligible for vote or not
age1=19
if age1>=18:
    print("Person is eligible for voting")

#Example 2 for if...else: Print if person is eligible for vote or not
age=15
if age>=18:
    print("Person is eligible for voting")
else:
    print("Person is not eligible for voting")

#Example 3 for if...else: Print if condtion is True or False using boolean value(True/False)
if True:
    print('Condition is True')
else:
    print('Condition is False')

#Example 4 for if...else: Print if condtion is True or False using boolean value(1/0)
if 1:
    print("Condition is True")
else:
    print("Condition is False")

#Example 5 for if...else: Print if number is odd or even
num=19
if num%2==0:
    print("Number is Even")
else:
    print("Number is Odd")

#Example 6 for if...esle: if..else statment write in single line (tertaory operator)
num=10
print("Number is Even") if num%2==0 else print("Number is odd")

#Example 7 for if...esle: if..else statment write in multiple statment (tertaory operator)
a=12
{print("Hello"),print("Python")} if a>=10 else {(print("hi"),print("JAVA"))}

#Example 7 for elif: Multiple conditions using elif

WeekNo=5
if WeekNo==1:
    print("Sunday")
elif WeekNo==2:
    print("Monday")
elif WeekNo==3:
    print("Teausday")
elif WeekNo==4:
    print("Wedensday")
elif WeekNo==5:
    print("Thursday")
elif WeekNo==6:
    print("Friday")
elif WeekNo==7:
    print("Saturday")
else:
    print("Invalid Number")


