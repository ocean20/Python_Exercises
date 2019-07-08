#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 16:17:32 2019

@author: cawang

function arguments

"""

def printme(s):
    print(s)

printme(s = "Keyword argument")

printme("This is a required argument")

# multiple arguments
def printinfo(name, age):
    print("Name:", name)
    print("Age:", age)
    
printinfo("Cathy", 12) # using required arguments
printinfo(12,"Cathy") # 12 was determined as the name -- took arguments based on position

printinfo(age = 12, name = "Cathy") # order of parameters doesn't matter if you have the keywords
printinfo(name = "Cathy", age = 12)

# Default arguments
def info(name, age = 35): 
    print("Name:", name)
    print("Age:", age)
    
info("Dad") # age will be 35 by default
info("Dad", 50) # age will be 50

def info2(age = 40, name):
    print("Name:", name)
    print("Age:", age)
    
info2(60, "Dad")
# error: on-default argument follows default argument
# you must put the default argument last

# Variable length arguments
def printVar(arg1, *vartuple):
    print("Output is:")
    print(arg1)
    for var in vartuple:
        print("Var is:", var)
        

printVar(10) # outputs 10, no other variable outputs
printVar(10, 15, 20) # 10 is arg1, 15 and 20 are *vartuple
# Output is:
# 10
# Var is: 15
# Var is: 20

# Anonymous functions
sum = lambda arg1, arg2: arg1 + arg2
print("The sum is:", sum(10,20)) # The sum is : 30

# return statement
def multiply(arg3, arg4):
    product = arg3 * arg4
    return product
result = multiply(15,10) # result = 150
print("Product is:", result) # PRoduct is: 150






