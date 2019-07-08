#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 15:58:29 2019

@author: cawang
"""

a = 3
b = a

id(a)
id(b)

a = a + 2
print(a) # a = 5
id(a) # a's address changed

print(b) # b still is 3
id(b) # b's address is still the same

x = [1,2,3]
y = x
x = [10, 12, 13]
print(y) #[1,2,3]
print(x) # [10,12,13]

l1 = [2,3,4]
l2 = l1
l1[0] = 24 # in place change
print(l1) # [24,3,4]
print(l2) # [24,3,4]

l1.append(5)
print(l1)
print(l2)


