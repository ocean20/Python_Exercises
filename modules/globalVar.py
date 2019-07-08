#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 19:17:41 2019

@author: cawang
"""

Money = 2000
def AddMoney():
    Money = Money + 1

print(Money)
AddMoney()
# no local variable Money inside function, so there is an error
print(Money)

def AddMoney2():
    global Money
    Money = Money + 1

AddMoney2()
print(Money) # 2001



