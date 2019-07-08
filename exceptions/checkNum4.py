#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 18:57:12 2019

@author: cawang

Display error message when we don't know the error name
"""

x = input("Enter a number: ")
num_x = int(x)

y = 100

try: 
    z = y * 1.0 / x
    print("Z is {}".format(z))
except Exception as e:
    print(str(e))