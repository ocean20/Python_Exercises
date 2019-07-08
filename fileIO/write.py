#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 14:56:07 2019

@author: cawang
"""

fo = open("fileWrite.txt", "a")
print("Name of file:", fo.name)

s = "This is 6th line"
fo.write("This is 6th line\n")
