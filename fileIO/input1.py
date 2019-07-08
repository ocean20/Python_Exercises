#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 14:14:15 2019

@author: cawang
"""

s = raw_input("Enter your input: ") # raw_input is on Python2.x
print("Received input:", s)

s2 = input("Enter your input: ") # input is on Python 3.x
print("Received input:", s2)
# Received input: 5*3

s3 = eval(input("Enter your input: ")) # eval(input()) assumes the input is a valid expression
print("Received input:", s3)
# if s3 = 5*3, received input will be 15
# Enter your input: [x*5 for x in range(2,10,2)]
# Received input: [10, 20, 30, 40]

