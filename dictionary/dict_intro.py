#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 18:30:09 2019

@author: cawang
"""

dic = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dic['Name'])
# Zara

print(dic['Gender'])
# gives a key error because it does not exist

print("Gender: ")
print(dic.get('Gender')) # prints "None"
print(dic.get('Gender', 'Gender not entered'))

print(dic.get('Name'))

# delete dictionary elements
del dic['Name'] # remove entry with key name
dic.clear() # remove all entries
del dic # delete dic variable --> printing dic gives 'dic' is not defined

# keys must be immutable
# you can use strings, numbers, or tuples as dictionary keys
# you cannot use lists as keys because lists are mutable

if 'Name' in dic:
    print(dic['Name'])
    
dic.items()
# dict_items([('Name', 'Zara'), ('Age', 7), ('Class', 'First')]
# returns list of tuple pairs

dic.keys()
# dict_keys(['Name', 'Age', 'Class'])

list(dic.values()) # make output a list
