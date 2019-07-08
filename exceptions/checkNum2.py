#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 18:49:47 2019

@author: cawang
"""

x = input("Enter a number: ")
num_x = int(x)

y = 100

try: 
    z = y * 1.0 / x
    print("Z is {}".format(z))
except ZeroDivisionError:
    print("Cannot divide by 0")
    