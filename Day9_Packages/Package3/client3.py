import sys
sys.path.append("C:/Users/dhananjay.pokale/Desktop/AWS_practice/Python_Learning/pythonFirstProject/Day9_Packages/Package1")
sys.path.append("C:/Users/dhananjay.pokale/Desktop/AWS_practice/Python_Learning/pythonFirstProject/Day9_Packages/Package2")

#Approach 1:
import EMP_Module
E_Obj=EMP_Module.Employee(100,"JHON",50000)
E_Obj.displayEmp()

import Stu_Module
S_Obj=Stu_Module.Students(101,"Shyam",'B')
S_Obj.displaystu()

#Approach 2:
from EMP_Module import Employee
E_Obj1=Employee(101,"Karan",20000)
E_Obj1.displayEmp()

from Stu_Module import Students
S_Obj1=Students(11,"Pawan",'C')
S_Obj1.displaystu()