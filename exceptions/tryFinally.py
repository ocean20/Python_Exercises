#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 19:08:56 2019

@author: cawang

finally block: put any code that must execute, whether the try-block raised
an exception or not

*you cannot use else clause along with a finally clause

"""
try:
    print(x)
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling")
except NameError as e:
    print(str(e))
finally:
    print("Error finding file and reading data")
    

    
# output: name 'x' is not defined
# Error finding file and reading data
    
'''
there is an error in print(x) --> except NameError catches and prints the error message


the finally block is executed
'''
