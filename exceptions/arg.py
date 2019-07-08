#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 19:51:56 2019

@author: cawang
"""

def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
        print(Argument)

# call function
temp_convert('xyz')

# Argument: invalid literal for int() with base 10: 'xyz'
 
    