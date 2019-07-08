#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 18:33:46 2019

@author: cawang
"""

fh = open("testfile", "r")
# FileNotFoundError: [Errno 2] No such file or directory: 'testfile'

line = fh.readline()
print(line)