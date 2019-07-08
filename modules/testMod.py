#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 19:03:25 2019

@author: cawang
"""

import aname

aname.print_func("Zara")
# Hello: Zara

content = dir(aname)
print(content)
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'print_func']

print(aname.__file__) # prints file path: /Users/cawang/Programming/Python/Python_Exercises/modules/aname.py
print(aname.__loader__)
print(aname.__name__) # module name: aname
print(aname.__package__)
