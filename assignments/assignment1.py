#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 12:17:21 2019

@author: cawang
"""

my_string = "Hello World" 
# creates a string "Hello World" and assigns the name my_string to it
id(my_string) # 4706066032

another_string = "Hello World"
id(another_string) # 4706373936
# created an independent copy

# instances where independent copies are not created
my_string2 = "hello"
id(my_string2) # 4706380688

another_string = "hello"
id(another_string) # 4706380688
# strings without whitespaces and less than 20 characters,
# integers from -5 to 255 are always reused to save memory

my_num = 5
id(my_num) # 4340536864
another_num = 5
id(another_num) # 4340536864

# when the right hand side is an existing variable
another_string = my_string
id(another_string) # 4706066032
# nothing is created in memory
# after the assignment, both variables refer to the already existing object
# (basically like giving the existing object a nickname)

another_string = "hello2"
# recreates another memory
print(my_string) # still is "Hello World"
print(another_string)


# how to copy a mutable object
my_list = [1,2,3]
id(my_list)
copy_my_list = my_list.copy() # independent copy
id(copy_my_list)
# the copies have different memory addresses

# copying an immutable object explicitly doesn't work

# adding an element to an immutable object
# since tuples are immutable, any operation that leads to a changed tuple
# would result in an independent copy
another_tuple = (1,2,3) 
id(another_tuple) # 4746112520
another_tuple += (4,) # (1,2,3,4)
id(another_tuple) # 4745688168
# * copies of immutable objects are created automatically under the hood

# adding an element to mutable object
my_list2 = [1,2,3]
another_list2 = my_list2 # both variables point to same object
another_list2 += [4,]
print(another_list2)
# [1, 2, 3, 4]
print(my_list2)
# [1, 2, 3, 4]
# in this ex. the mutable object was modified in place with the +=
# Python calls __iadd__

my_list3 = [1,2,3]
another_list3 = my_list3
another_list3 = another_list3 + [4,]
print(another_list3)
# [1, 2, 3, 4]
print(my_list3)
# [1, 2, 3]
# Python calls __add__ which returns a new copy instead of 
# modifying the list in place