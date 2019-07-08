#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 20:51:08 2019

@author: cawang
"""

from draw import draw_game

def main():
    # draw.draw_game() # this is ok
    draw_game() # this is ok too because from draw.py file, we imported the draw_game() function. main knows the function
    

if __name__ == '__main__':
    main()
    
    
