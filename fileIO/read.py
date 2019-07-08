#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 15:20:40 2019

@author: cawang
"""

fo = open("fileRead.txt", "r+")
s = fo.read(10) # number of bytes to be read from the opened file
print("String read:", s)
# String read: Read this 


# check current position
pos = fo.tell()
print("Current position:", pos) # 10

# reposition pointer to beginning
pos = fo.seek(0,0)
print("Again read string is:", s)
# Again read string is: Read this

fo.close()

