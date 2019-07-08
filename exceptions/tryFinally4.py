#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 19:23:19 2019

@author: cawang
"""

try: 
    fh = open("testfile", "w")
    try:
        fh.write("this is my test file for exception handling")
    finally:
        print("going to close the file")
        fh.close()
except:
    print("Error found")
    
# output: going to close the file

""""
since there is no error in fh = open, it goes to the inner try block

the inner try passes to the finally block

after the finally block is excecuted, it will go to the outer except statement


"""
