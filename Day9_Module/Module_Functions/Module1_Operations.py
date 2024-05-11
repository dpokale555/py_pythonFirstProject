#Approach 1: to import the functions from other module
import Module1_Calculator
Module1_Calculator.add(100, 200)
Module1_Calculator.mult(10, 20)

#Approach 2: to import the specific fucntions from other module
from Module1_Calculator import add,mult
add(100,200)
mult(10,20)

#Approach 3: to import all the fucntions from other module
from Module1_Calculator import *
add(100,200)
mult(10,20)
