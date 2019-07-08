#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 14:35:40 2019

@author: cawang
"""

# open file
fo = open("testFile.txt", "w+")
print("Name of file:", fo.name)
print("Opening mode:", fo.mode)

fo.write("This is a line of text") # this rewrote what was in the file
# ouptputs the number of characters written
 
fo.close()

# open another file
f = open("testFile2.txt", "a")
print("Name of file:", f.name)
print("Opening mode:", f.mode)

f.write("This is another line") # added "This is another line" to existing file