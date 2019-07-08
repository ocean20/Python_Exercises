#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 19:21:38 2019

@author: cawang
"""

try: 
    fh = open("testfile", "r")
    try:
        fh.write("this is my test file for exception handling")
    finally:
        print("going to close the file")
        fh.close()
except IOError:
    print("Error found")

# Error found
    
# outside try block matches with except block