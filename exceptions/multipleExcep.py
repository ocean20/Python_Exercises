#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 19:03:16 2019

@author: cawang
"""

try: 
    
    # print("read this")
    fh = open("testfile", "r")
    print("does this work")
    line = fh.readline()
    print(line)
    print("hello")
# except FileNotFoundError:  # python 2.x
#     print("Error: file not found")
except(IOError,ZeroDivisionError) as e: # python 3.7
    print(str(e))
except: 
    print("Error found")
    
print("After except") # will run after exception