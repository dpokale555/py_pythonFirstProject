#Approach 1: In case of same fucntion in two module
import Module2_Animal
import Module2_Bird

Module2_Animal.fly()
Module2_Animal.color()

Module2_Bird.fly()
Module2_Bird.color()

#Appraoch 2: In case of same function in two module
from Module2_Animal import *
fly()
color()
from Module2_Bird import *
fly()
color()


