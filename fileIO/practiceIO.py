#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 15:33:50 2019

@author: cawang
"""

X, Y, Z = 43, 44, 45
S = 'Spam' # Must be strings to store in file
D = {'a':1, 'b': 2}
L = [1, 2, 3]

fo = open('datafile.txt', 'w')
fo.write(S + '\n')

fo.write('%s,%s,%s\n' % (X,Y,Z)) # Convert numbers to string
fo.write(str(L) + '$' + str(D) + '\n') # Convert and separate with $

fo.close()

content = open('datafile.txt').read() # content: "Spam\n43,44,45\n[1, 2, 3]${'a': 1, 'b': 2}\n" <-- raw bytes display
print(content) 
# Spam
# 43,44,45
# [1, 2, 3]${'a': 1, 'b': 2}

# Conversions
fo = open('datafile.txt')
line = fo.readline() # read one line
# line: 'Spam\n'
line2 = line.rstrip() # remove end of line; could also do line[:-1]
# line2: 'Spam'

line_num = fo.readline() # read next line
print(line_num) # 43, 44, 45
type(line_num) # str
parts = line_num.split(',')
print(parts) # ['43', '44', '45\n']
nums = [int(p) for p in parts] # convert all in list at once
print(nums)
# [43, 44, 45]
