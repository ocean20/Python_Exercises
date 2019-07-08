#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 18:35:52 2019

@author: cawang
"""


try: 
    print(x)
    # print("read this")
    fh = open("testfile", "r")
    print("does this work")
    line = fh.readline()
    print(line)
    print("hello")
# except FileNotFoundError:  # python 2.x
#     print("Error: file not found")
except IOError: # python 3.7
    print("Error: IOError")
except: 
    print("Error found")
    
print("After except") # will run after exception
    