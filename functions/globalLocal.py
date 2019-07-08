#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 16:41:56 2019

@author: cawang
"""

x = 2
def fun1():
    x = 1
    print("Inside function x =", x)

fun1() # Inside function x = 1
print("Outside function x =", x) # Outside function x = 2

def fun2():
    print("Inside function x =", x)

fun2() # Inside function x = 2 
# the function did not declare a local variable x, so it looked for the global one

def fun3():
    print("Inside function x =", x)
    x = 3
    print("Inside function x after change:", x)

fun3()
# error: local variable 'x' referenced before assignment


