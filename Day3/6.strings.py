######cretate strings variable#########
a="welcomeA"
b='welcomeB'
s=str("Welcome1")
t=str('Welcome2')

#######crteating empty strings variables##########
name=""
name=''
name=str()

#########immutable/mutable###############
#mutable : can not change the value of the variables
#Immutable : can change the value of the variables
#string is immutables variables

str1='welcome5'
print(id(str1))     #2872425594352

str1=str1+"to pytghon"
print(id(str1))

############ + and * with string ###############
str='Welcom '
print(str+'python')        #Welcom python
print(str*3)               #Welcom Welcom Welcom

########## Slicing operator ###########################
#starting index is always '0'
#ending index is 1
str2='Hello'
print(str2[1:3])     #el
print(str2[:4])      #Hell
print(str2[2:])      #llo
print(str2[1:-1])    #ell

############### ord(), chr() ###############
print(ord('A'))    #65 #return the ASCII code of the charechter
print(chr(65))     #A #return the charechter represented by ASCII numbers

############## max(), min(), len() ################
print(max('abcd'))      #d
print(min('abcd'))      #a
print(len('abcd'))      #4 ---length

############# in, not  in operators ################
str4='welcome'
print("come" in str4)   #True
print("lome" in str4)   #False

print("lome" not in str4)   #True
print("come" not in str4)   #False


############ string comparisons #####################
print("tim" == "tie")
print("free" != "freedom")
print("arrow" > "aron")
print("right" >= "left")
print("teeth" < "tee")
print("yellow" <= "fellow")
print("abc" > "")

###### Teststing strings TRue/False##################
str5="welcome to python"
print(str5.isalnum())
print("Hello".isalpha())
print("2012".isdigit())
print("first number".isidentifier())
print(str5.islower())
print("HELLOW".isupper())
print(" ".isspace())
print(str5.endswith("thon"))
print(str5.startswith("good"))
print(str5.find("come"))
print(str5.find("become"))
print(str5.count("o"))

###### Converting strings ##################
str5="welcome to python"
print(str5.capitalize())                         #Welcome to python
print(str5.title())                              #Welcome To Python
print(str5.lower())                              #welcome to python
print(str5.upper())                              #WELCOME TO PYTHON
print(str5.swapcase())                           #WELCOME TO PYTHON
print(str5.replace("co", "tk"))     #weltkme to python

###### How to reverse string ##################
#Method1
str6="welcome"
rev_str=""
for i in str6:
    rev_str=i+rev_str
print("Reverse string is :",rev_str)

#Method2
str7="welcome"
rev_str=str7[::-1]     #[start:end:increment/decrement] i.e [0:7:-1]
print(rev_str)
