#Approach 1:
import Class1_Animal
import Class1_Bird

Obj_A=Class1_Animal.Animal()
Obj_A.display()

Obj_B=Class1_Bird.Bird()
Obj_B.bird()


#Approach 2:
from Class1_Animal import Animal
from Class1_Bird import Bird

Obj_1=Animal()
Obj_1.display()

Obj_2=Bird()
Obj_2.bird()