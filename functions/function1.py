#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 18:57:59 2019

@author: cawang
"""


def printme(mystring):
    "This prints a string" # this is like a comment
    print(mystring)
    mystring = "12"
    return

s = "I am the first string"
print("first string s:")
printme(s)

print("changed string s:")
print(s)

# pass by reference
'''
the function did not make a copy of the contents. the address(reference) of the variable
is obtained by the function. the function makes changes to that variable. so when you print
the original variable, it is changed too. 
'''

# pass by value
'''
in the function: variable's contents are copied to the function area (stack). 
the function will only change the values in the local stack, it does not change
the variable in the main program.
'''

def printlist(mylist):
    mylist.append([1,2,3,4])
    print("Values inside the function:", mylist)
    
a = [10, 20, 30, 40]
printlist(a)
print("Values outside the function:", a)
# originally a: [10, 20, 30, 40]
# after running function a: [10, 20, 30, 40, [1, 2, 3, 4]]


