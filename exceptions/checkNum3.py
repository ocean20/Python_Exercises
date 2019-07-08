#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 18:52:06 2019

@author: cawang

Instead of printing your own message, print the default error message
"""

x = input("Enter a number: ")
num_x = int(x)

y = 100

try: 
    z = y * 1.0 / x
    print("Z is {}".format(z))
except ZeroDivisionError as e:
    print(str(e))
    # ZeroDivisionError: float division by zero <-- this is the error's error message
    # output: float division by zero
