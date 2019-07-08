# -*- coding: utf-8 -*-
"""
Write a program (function!) that takes a list and returns a new list 
that contains all the elements of the first list minus all the duplicates.

Write two different functions to do this - one using a loop and constructing 
a list, and another using sets.
"""

# function method
def remove_dup(x):
    y = []
    for i in x:
        if i not in y:
             y.append(i)
             
    return y


a = [3,2,1,1,7,10,12,12,15]
way1 = remove_dup(a)
print(way1)
# [3, 2, 1, 7, 10, 12, 15]


# set method
def diff_list(num):
    return list(set(num))

way2 = diff_list(a)
print(way2)
# [1, 2, 3, 7, 10, 12, 15]

"""
converting from set to list
  names = ["Michele", "Robin", "Sara", "Michele"]
  names = set(names)
  names = list(names)
  print(names)
"""