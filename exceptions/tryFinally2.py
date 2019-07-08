#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 19:13:43 2019

@author: cawang
"""

try: 
    fh = open("testfile", "r")
    try:
        fh.write("this is my test file for exception handling")
    finally:
        print("going to close the file")
        fh.close()
except:
    print("Error found")
finally:
    print("After the try block")

# output: Error found
# After the try block
    
'''
there is an error in fh = open
'''