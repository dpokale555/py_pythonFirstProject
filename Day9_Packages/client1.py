import sys
sys.path.append("C:/Users/dhananjay.pokale/Desktop/AWS_practice/Python_Learning/pythonFirstProject/Day9_Packages/Pack1")

#Approach 1:
import module1
import module2

module1.display()
module2.show()

#Approach 2:
from module1 import *
from module2 import *

module1.display()
module2.show()