#Approach 1:
import sys
sys.path.append("C:/Users/dhananjay.pokale/Desktop/AWS_practice/Python_Learning/pythonFirstProject/Day9_Packages/Pack2")
sys.path.append("C:/Users/dhananjay.pokale/Desktop/AWS_practice/Python_Learning/pythonFirstProject/Day9_Packages/Pack2/Pack22")

import module1
module1.display()

import module2
module2.show()

#Approach 2:
import sys
sys.path.append("C:/Users/dhananjay.pokale/Desktop/AWS_practice/Python_Learning/pythonFirstProject/Day9_Packages/Pack2")
sys.path.append("C:/Users/dhananjay.pokale/Desktop/AWS_practice/Python_Learning/pythonFirstProject/Day9_Packages/Pack2/Pack22")

from module1 import *
from module2 import *

display()
show()


